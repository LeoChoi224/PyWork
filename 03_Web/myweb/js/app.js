/**
 * 화면 이동 라우팅 및 이벤트 처리
 */

document.addEventListener("DOMContentLoaded", () => {
    // 기본 포스터 렌더링
    renderPosterGrid(defaultMovies);

    // 시작 버튼
    const startBtn = document.getElementById("start-btn");
    console.log(startBtn);

    // 시작 버튼 -> 모달 열기
    startBtn?.addEventListener("click", openModal);

    // 추천 받기 버튼
    const recommendBtn = document.getElementById("recommend-btn");
    console.log(recommendBtn);

    recommendBtn
        .addEventListener("click", async (e) => {
            e.preventDefault();
            try {
                // 기존 입력폼 숨기고 로딩 출력
                renderLoading("영화 추천 비서가 취향을 분석 중입니다... 잠시 기다려주십시오.");

                // 추천 시스템 실행
                const result = await runRecommendationFlow();

                if (!result?.ok) {
                    renderError(result?.message || "추천을 완료하지 못했습니다.");
                    return;
                }

                renderMovieCards(result.recommendations, result.displayText);
                closeModal();
                showResultSection();

                document.querySelectorAll("[data-close-modal]").forEach((el) => {
                    el.addEventListener("click", closeModal);
                });

                document.addEventListener("keydown", (e) => {
                    if (e.key === "Escape" && modalRoot && !modalRoot.hidden) {
                        closeModal();
                    }
                });

            } catch (error) {
                console.error(error);
                renderError("추천 생성 중 오류가 발생했습니다.");
            }
        });
});

const body = document.body; // body 요소
const modalRoot = document.getElementById("modal-root"); // 모달 최상위 컨테이너
const navOpenForm = document.getElementById("nav-open-form"); // 네비 '취향 입력' 링크
/**
 * 모달 열기
 */
function openModal() {
    if (!modalRoot) return; // 요소 없으면 종료
    modalRoot.hidden = false; // HTML hidden 속성 제거
    modalRoot.setAttribute("aria-hidden", "false"); // 스크린리더: 보임
    requestAnimationFrame(function () { // 다음 프레임에 클래스 추가 (transition)
        modalRoot.classList.add("is-open"); // 모달 카드 fade-in
        body.classList.add("is-modal-visible"); // 배경 blur
    });
    document.getElementById("gender")?.focus(); // 첫 입력란에 포커스
}

/** 
 * 모달 닫기 
 */
function closeModal() {
    if (!modalRoot) return;
    modalRoot.classList.remove("is-open"); // 애니메이션 시작
    body.classList.remove("is-modal-visible"); // blur 제거
    modalRoot.setAttribute("aria-hidden", "true");
    setTimeout(function () { // transition 0.3s 후
        modalRoot.hidden = true; // DOM에서 숨김
    }, 300);
}

/* ——— 이전에 입력한 값 복원 (새로고침·재방문) ——— */
// const STORAGE_KEY = "moviepick_user"; // sessionStorage에 저장할 사용자 정보 키
// const saved = sessionStorage.getItem(STORAGE_KEY);
// if (saved && form) {
//     try {
//         const data = JSON.parse(saved); // JSON 파싱
//         if (data.gender) form.gender.value = data.gender;
//         if (data.age) form.age.value = data.age;
//         if (data.mbti) form.mbti.value = data.mbti;
//         if (data.mood) form.mood.value = data.mood;
//     } catch (_) { /* JSON 깨져 있으면 무시 */ }
// }
