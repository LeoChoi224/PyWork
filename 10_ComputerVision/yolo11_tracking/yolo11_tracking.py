# 사전 설치 : pip install ultralytics


# yolo11_tracking_test_data.zip

# 테스트 데이터 ski.mp4 / airport.mp4
# 객체추적 (object tracking) 을 테스트 하기 위해 pixabay(pixabay.com) 에서 무료로 제공되는 동영상을 사용해봅니다.
# - 속도감이 느껴지는 동영상 (ski.mp4)
# - 다양한 객체가 존재하는 동영상 (airport.mp4) 


import argparse
from ultralytics import YOLO


if __name__ == '__main__':

	# command line argument 체크 
	parser = argparse.ArgumentParser()
	parser.add_argument('arg1')
	args = parser.parse_args()

	print('😎', args.arg1)

	# 사전 학습된 (pre-trained) YOLO model loading 
	model = YOLO("yolo11n.pt")

	# 영상 tracking
	results = model.track(args.arg1, save=True, show=True)

# 실행
# python yolo11_tracking.py ski.mp4

#   결과: 별도의 창이 떠서 tracking 영상
#   실행종료는 CTRL + C

#   runs\detect\track\ski.avi 파일 생김  <- tracknig 결과 영상


# python yolo11_tracking.py airport.mp4
#   runs\detect\track-2\airport.avi 파일 생김