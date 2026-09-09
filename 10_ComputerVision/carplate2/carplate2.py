import cv2
import os, sys
import re
import time
import numpy as np
import pytesseract


# ══════════════════════════════════════════════════════════════
# 설정값
# ══════════════════════════════════════════════════════════════
# 3단계 : 글자 후보 선별 (영상 속 번호판이 작아서 수업값보다 낮춤)
MIN_AREA = 40
MIN_WIDTH, MIN_HEIGHT = 2, 7
MIN_RATIO, MAX_RATIO = 0.2, 1.0

# 4단계 : 배치로 번호판 그룹 찾기
MAX_DIAG_MULTIPLYER = 4.0
MAX_ANGLE_DIFF = 10.0
MAX_AREA_DIFF = 0.4
MAX_WIDTH_DIFF = 0.6
MAX_HEIGHT_DIFF = 0.25
MIN_N_MATCHED = 4

# 5단계 : 번호판 잘라내기 (넓게 자르고 7단계에서 다듬는다)
PLATE_WIDTH_PADDING = 2.0
PLATE_HEIGHT_PADDING = 1.7
MIN_PLATE_RATIO, MAX_PLATE_RATIO = 2.5, 9.0

# 7~8단계 : OCR
TARGET_H = 64                      # 번호판 crop 을 이 높이로 확대
MIN_PLATE_CHARS = 4
OCR_CFG = ('--psm 7 --oem 1 '      # 수업의 --oem 0 은 brew tesseract 에 레거시 엔진이 없어 에러
           '-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

# 9단계 : 영국 번호판 형식 (글자2 + 숫자2 + 글자3)
PLATE_RE = re.compile(r'[A-Z]{2}\d{2}[A-Z]{3}')
TO_DIGIT = {'O': '0', 'Q': '0', 'D': '0', 'I': '1', 'L': '1', 'J': '1',
            'Z': '2', 'S': '5', 'B': '8', 'G': '6', 'T': '7', 'A': '4'}
TO_ALPHA = {'0': 'O', '1': 'I', '2': 'Z', '5': 'S', '8': 'B', '6': 'G',
            '4': 'A', '7': 'T'}

# 11~12단계 : 추적 / OCR 절약 (속도 최적화 핵심)
TRACK_MAX_MISS = 8                 # 8프레임 안 보이면 추적 종료
OCR_INTERVAL = 4                   # 4프레임에 1번만 OCR
MAX_OCR_PER_TRACK = 12             # 한 번호판당 OCR 최대 횟수
CONFIRM_VOTES = 3                  # 같은 답 3번이면 확정하고 OCR 중단
MIN_OCR_WIDTH = 55                 # 너무 작은 번호판은 OCR 안 함

# 표시 색상
BOX_COLOR = (0, 0, 255)            # 번호판 영역 : 붉은색
TEXT_COLOR = (0, 255, 255)         # 인식한 번호 : 노란색

possible_contours = []             # find_chars 가 참조하는 전역


# ══════════════════════════════════════════════════════════════
# 4단계 : 나란히 놓인 글자끼리 묶기
# ══════════════════════════════════════════════════════════════
def find_chars(contour_list):
    matched_result_idx = []

    for d1 in contour_list:
        matched_contours_idx = []

        for d2 in contour_list:
            if d1['idx'] == d2['idx']:
                continue

            dx = abs(d1['cx'] - d2['cx'])
            dy = abs(d1['cy'] - d2['cy'])
            distance = np.linalg.norm(np.array([d1['cx'], d1['cy']]) -
                                      np.array([d2['cx'], d2['cy']]))
            diagonal_length1 = np.sqrt(d1['w'] ** 2 + d1['h'] ** 2)

            if dx == 0:
                angle_diff = 90
            else:
                angle_diff = np.degrees(np.arctan(dy / dx))

            area_diff = abs(d1['w'] * d1['h'] - d2['w'] * d2['h']) / (d1['w'] * d1['h'])
            width_diff = abs(d1['w'] - d2['w']) / d1['w']
            height_diff = abs(d1['h'] - d2['h']) / d1['h']

            if distance < diagonal_length1 * MAX_DIAG_MULTIPLYER \
            and angle_diff < MAX_ANGLE_DIFF and area_diff < MAX_AREA_DIFF \
            and width_diff < MAX_WIDTH_DIFF and height_diff < MAX_HEIGHT_DIFF:
                matched_contours_idx.append(d2['idx'])

        matched_contours_idx.append(d1['idx'])

        if len(matched_contours_idx) < MIN_N_MATCHED:
            continue

        matched_result_idx.append(matched_contours_idx)

        unmatched_contour_idx = []
        for d4 in contour_list:
            if d4['idx'] not in matched_contours_idx:
                unmatched_contour_idx.append(d4['idx'])

        # idx 는 possible_contours 기준 번호이므로 거기서 꺼내야 한다
        unmatched_contour = np.take(possible_contours, unmatched_contour_idx)

        for idx in find_chars(unmatched_contour):
            matched_result_idx.append(idx)

        break

    return matched_result_idx


# ══════════════════════════════════════════════════════════════
# 6단계 : 겹치는 박스 정리
# ══════════════════════════════════════════════════════════════
def remove_overlap(plate_imgs, plate_infos, thresh=0.3):
    order = sorted(range(len(plate_infos)),
                   key=lambda i: -(plate_infos[i]['w'] * plate_infos[i]['h']))

    keep_imgs, keep_infos = [], []
    for i in order:
        px, py = plate_infos[i]['x'], plate_infos[i]['y']
        pw, ph = plate_infos[i]['w'], plate_infos[i]['h']

        overlapped = False
        for k in keep_infos:
            X, Y, W, H = k['x'], k['y'], k['w'], k['h']
            iw = max(0, min(px + pw, X + W) - max(px, X))
            ih = max(0, min(py + ph, Y + H) - max(py, Y))
            if iw * ih / min(pw * ph, W * H) > thresh:
                overlapped = True
                break

        if not overlapped:
            keep_imgs.append(plate_imgs[i])
            keep_infos.append(plate_infos[i])

    return keep_imgs, keep_infos


# ══════════════════════════════════════════════════════════════
# 2~6단계 : 프레임 한 장에서 번호판 영역 찾기
# ══════════════════════════════════════════════════════════════
def detect_plates(frame):
    global possible_contours

    height, width, channel = frame.shape

    # 2단계 : 흑백 -> 블러 -> 이진화
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(gray, ksize=(5, 5), sigmaX=0)
    img_blur_thresh = cv2.adaptiveThreshold(img_blurred, 255.0,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY_INV,
                                            blockSize=19, C=9)

    # 3단계 : 윤곽선 -> 글자 후보
    contours, _ = cv2.findContours(img_blur_thresh,
                                   mode=cv2.RETR_LIST,
                                   method=cv2.CHAIN_APPROX_SIMPLE)

    possible_contours = []
    cnt = 0
    for contour in contours:
        cx_, cy_, cw_, chh_ = cv2.boundingRect(contour)
        if chh_ == 0:
            continue
        area = cw_ * chh_
        ratio = cw_ / chh_
        if area > MIN_AREA and cw_ > MIN_WIDTH and chh_ > MIN_HEIGHT \
        and MIN_RATIO < ratio < MAX_RATIO:
            possible_contours.append({'x': cx_, 'y': cy_, 'w': cw_, 'h': chh_,
                                      'cx': cx_ + (cw_ / 2), 'cy': cy_ + (chh_ / 2),
                                      'idx': cnt})
            cnt += 1

    if len(possible_contours) < MIN_N_MATCHED:
        return [], []

    # 4단계 : 배치로 그룹 만들기
    result_idx = find_chars(possible_contours)

    # 5단계 : 회전 보정 후 잘라내기
    plate_imgs, plate_infos = [], []

    for idx_list in result_idx:
        matched_chars = np.take(possible_contours, idx_list)
        sorted_chars = sorted(matched_chars, key=lambda d: d['cx'])

        plate_cx = (sorted_chars[0]['cx'] + sorted_chars[-1]['cx']) / 2
        plate_cy = (sorted_chars[0]['cy'] + sorted_chars[-1]['cy']) / 2
        plate_width = (sorted_chars[-1]['x'] - sorted_chars[0]['x'] +
                       sorted_chars[-1]['w']) * PLATE_WIDTH_PADDING

        sum_height = 0
        for d in sorted_chars:
            sum_height += d['h']
        plate_height = int((sum_height / len(sorted_chars)) * PLATE_HEIGHT_PADDING)
        if plate_height == 0:
            continue

        triangle_height = sorted_chars[-1]['cy'] - sorted_chars[0]['cy']
        triangle_hypotenus = np.linalg.norm(
            np.array([sorted_chars[0]['cx'], sorted_chars[0]['cy']]) -
            np.array([sorted_chars[-1]['cx'], sorted_chars[-1]['cy']]))

        if triangle_hypotenus == 0:
            angle = 0.0
        else:
            angle = np.degrees(np.arcsin(triangle_height / triangle_hypotenus))

        rotation_matrix = cv2.getRotationMatrix2D(center=(plate_cx, plate_cy),
                                                  angle=angle, scale=1.0)
        img_rotated = cv2.warpAffine(gray, M=rotation_matrix, dsize=(width, height))
        img_cropped = cv2.getRectSubPix(img_rotated,
                                        patchSize=(int(plate_width), int(plate_height)),
                                        center=(int(plate_cx), int(plate_cy)))

        if img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO \
        or img_cropped.shape[1] / img_cropped.shape[0] > MAX_PLATE_RATIO:
            continue

        plate_imgs.append(img_cropped)
        plate_infos.append({'x': int(plate_cx - plate_width / 2),
                            'y': int(plate_cy - plate_height / 2),
                            'w': int(plate_width),
                            'h': int(plate_height)})

    # 6단계 : 겹치는 박스 정리
    return remove_overlap(plate_imgs, plate_infos)


# ══════════════════════════════════════════════════════════════
# 7단계 : 번호판에서 글자 범위만 다시 찾아 다듬기
# ══════════════════════════════════════════════════════════════
def refine_plate(crop):
    if crop is None or crop.shape[0] < 5:
        return None

    scale = TARGET_H / crop.shape[0]
    img = cv2.resize(crop, dsize=(0, 0), fx=scale, fy=scale,
                     interpolation=cv2.INTER_CUBIC)
    _, binary = cv2.threshold(img, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # findContours 는 흰색을 찾으므로 반전해서 넣는다
    contours, _ = cv2.findContours(cv2.bitwise_not(binary),
                                   mode=cv2.RETR_LIST,
                                   method=cv2.CHAIN_APPROX_SIMPLE)

    ch, cw = binary.shape
    boxes = []
    for contour in contours:
        bx, by, bw, bh = cv2.boundingRect(contour)
        if bh < ch * 0.25 or bh > ch * 0.90:   # 잡티 / 번호판 테두리 제외
            continue
        if bw < 2 or bw > bh * 1.2:            # 가로로 퍼진 테두리 선 제외
            continue
        boxes.append((bx, by, bw, bh))

    if len(boxes) < MIN_PLATE_CHARS:
        return None

    # 같은 줄에 나란히 있는 것만 남긴다 (EU 파란띠, 나사 자국 제거)
    med_h = np.median([b[3] for b in boxes])
    med_cy = np.median([b[1] + b[3] / 2 for b in boxes])

    keep = []
    for b in boxes:
        bcy = b[1] + b[3] / 2
        if abs(b[3] - med_h) < med_h * 0.32 and abs(bcy - med_cy) < med_h * 0.30:
            keep.append(b)

    if len(keep) < MIN_PLATE_CHARS:
        return None

    plate_min_x = min(b[0] for b in keep)
    plate_max_x = max(b[0] + b[2] for b in keep)
    plate_min_y = min(b[1] for b in keep)
    plate_max_y = max(b[1] + b[3] for b in keep)

    img_result = binary[max(plate_min_y - 3, 0):plate_max_y + 3,
                        max(plate_min_x - 3, 0):plate_max_x + 3]
    if img_result.size == 0:
        return None

    # 노이즈 제거 (blur + threshold)
    img_result = cv2.GaussianBlur(img_result, ksize=(3, 3), sigmaX=0)
    _, img_result = cv2.threshold(img_result, 0.0, 255.0,
                                  cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # tesseract 가 잘 읽도록 여백을 준다 (글자가 검정이므로 흰색 여백)
    return cv2.copyMakeBorder(img_result, 18, 18, 18, 18,
                              cv2.BORDER_CONSTANT, value=255)


# ══════════════════════════════════════════════════════════════
# 8~9단계 : OCR + 형식 교정
# ══════════════════════════════════════════════════════════════
def read_plate_raw(img_result):
    chars = pytesseract.image_to_string(img_result, lang='eng', config=OCR_CFG)
    return re.sub(r'[^A-Z0-9]', '', chars.upper())


def correct_format(text):
    """영국 번호판 형식(글자2+숫자2+글자3)에 맞춰 헷갈리는 글자를 고친다"""
    if len(text) != 7:
        return text, False

    fixed = ''
    for i, c in enumerate(text):
        if i in (2, 3):                 # 3, 4번째 자리는 숫자
            fixed += TO_DIGIT.get(c, c)
        else:                           # 나머지는 글자
            fixed += TO_ALPHA.get(c, c)

    return fixed, bool(PLATE_RE.fullmatch(fixed))


def read_plate(plate_img):
    img_result = refine_plate(plate_img)
    if img_result is None:
        return None, False
    return correct_format(read_plate_raw(img_result))


# ══════════════════════════════════════════════════════════════
# 11단계 : 프레임 사이에서 같은 번호판 이어붙이기
# ══════════════════════════════════════════════════════════════
def match_tracks(tracks, plate_infos):
    used = []

    for tr in tracks:
        tcx = tr['box']['x'] + tr['box']['w'] / 2
        tcy = tr['box']['y'] + tr['box']['h'] / 2

        best, best_dist = -1, None
        for i, info in enumerate(plate_infos):
            if i in used:
                continue
            icx = info['x'] + info['w'] / 2
            icy = info['y'] + info['h'] / 2
            dist = np.linalg.norm(np.array([icx, icy]) - np.array([tcx, tcy]))
            limit = max(tr['box']['w'], info['w']) * 0.6
            if dist < limit and (best_dist is None or dist < best_dist):
                best, best_dist = i, dist

        if best >= 0:
            used.append(best)
            tr['box'] = plate_infos[best]
            tr['miss'] = 0
            tr['cur'] = best
            tr['seen'] += 1
        else:
            tr['miss'] += 1
            tr['cur'] = -1

    return used


base_path = r'/Users/leo/LeoData/MyCode/KoreaITAcademy/LangChain/dataset/ComputerVision/carplate2'  # ← ★ 본인의 경로 입력!
# base_path = r'D:\KDT2604\dataset\ComputerVision\carplate2'  # ← ★ 본인의 경로 입력!

cap = cv2.VideoCapture(os.path.join(base_path, 'carplate2.mp4'))

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

if not cap.isOpened():
    print('camera open failed')
    sys.exit()

frame_cnt = 0

# ── 추가 : 추적/투표에 쓸 변수 ──
tracks = []
next_id = 0
ocr_calls = 0
found = {}
t_start = time.time()

while True:
    ret, frame = cap.read()
    if not ret:  break

    # ── 추가 : 검출 -> 추적 -> OCR -> 그리기 ──
    frame_cnt += 1

    # 1) 번호판 검출
    plate_imgs, plate_infos = detect_plates(frame)

    # 2) 기존 추적과 이어붙이기
    used = match_tracks(tracks, plate_infos)

    # 3) 새로 나타난 번호판 등록
    for i, info in enumerate(plate_infos):
        if i not in used:
            tracks.append({'id': next_id, 'box': info, 'miss': 0, 'cur': i,
                           'seen': 1, 'votes': {}, 'text': '',
                           'confirmed': False, 'ocr_count': 0, 'last_ocr': -999})
            next_id += 1

    # 4) 오래 안 보인 추적 종료
    tracks = [tr for tr in tracks if tr['miss'] <= TRACK_MAX_MISS]

    # 5) OCR — 필요한 것만 (가장 느린 부분이라 최대한 아낀다)
    for tr in tracks:
        if tr['cur'] < 0:                              continue
        if tr['confirmed']:                            continue
        if tr['ocr_count'] >= MAX_OCR_PER_TRACK:       continue
        if tr['box']['w'] < MIN_OCR_WIDTH:             continue
        if frame_cnt - tr['last_ocr'] < OCR_INTERVAL:  continue

        tr['last_ocr'] = frame_cnt
        tr['ocr_count'] += 1
        ocr_calls += 1

        text, ok = read_plate(plate_imgs[tr['cur']])

        if ok:
            tr['votes'][text] = tr['votes'].get(text, 0) + 1
            tr['text'] = max(tr['votes'], key=tr['votes'].get)

            if tr['votes'][tr['text']] >= CONFIRM_VOTES:
                tr['confirmed'] = True
                if tr['text'] not in found:
                    found[tr['text']] = frame_cnt
                    print(f'[frame {frame_cnt:4d}] 번호판 인식 : {tr["text"]}')

    # 6) 붉은 사각형 + 노란 글자 (번호판을 따라다닌다)
    for tr in tracks:
        if tr['miss'] > 0:          # 이번 프레임에 안 보이면 그리지 않는다
            continue

        px, py = tr['box']['x'], tr['box']['y']
        pw, ph = tr['box']['w'], tr['box']['h']

        cv2.rectangle(frame, pt1=(px, py), pt2=(px + pw, py + ph),
                      color=BOX_COLOR, thickness=2)

        if tr['text']:
            # 검은 테두리를 먼저 굵게 깔아 밝은 배경에서도 잘 보이게
            cv2.putText(frame, tr['text'], (px, py - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 5)
            cv2.putText(frame, tr['text'], (px, py - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, TEXT_COLOR, 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(delay) == 27:  # ESC 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()

# # ── 추가 : macOS 에서 창이 확실히 닫히도록 ──
# for _ in range(5):
#     cv2.waitKey(1)

# ── 추가 : 결과 요약 ──
elapsed = time.time() - t_start
print('-' * 55)
print(f'처리 프레임 {frame_cnt} / {elapsed:.1f}초  ({frame_cnt / elapsed:.1f} fps)')
print(f'OCR 호출 {ocr_calls}회')
print(f'인식한 번호판 {len(found)}개 : {", ".join(sorted(found))}')