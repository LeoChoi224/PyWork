/**
 * 화면 이동 라우팅 및 이벤트 처리
 */

/**
 * 현재 상세 영화
 */
let currentDetailMovie = null;

document.addEventListener("DOMContentLoaded", () => {
    // 기본 포스터 렌더링
    renderPosterGrid(defaultMovies);
    initModalClose();

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

            } catch (error) {
                console.error(error);
                renderError("추천 생성 중 오류가 발생했습니다.");
            }
        });

    document.addEventListener("click", async (e) => {
        const poster = e.target.closest(".item.thumb");
        if (!poster) return;

        const movieId = poster.dataset.movieId;
        if (!movieId) return;

        await openMovieDetail(movieId);
    });

    document.addEventListener("click", async (e) => {
        const movieCard = e.target.closest(".movie-card");
        if (!movieCard) return;

        const movieId = movieCard.dataset.movieId;
        if (!movieId) return;

        await openMovieDetail(movieId);
    });

    document.addEventListener("keydown", (e) => {
        if (e.key !== "Escape") return;
        const detailPage = document.getElementById("page-detail");

        if (detailPage && !detailPage.classList.contains("hidden")) {
            hideDetailPage();
        }
    });

    /**
     * 상세 페이지 버튼 이벤트
     */
    document.addEventListener("click", (e) => {
        /**
         * 추천 목록으로 가기
         */
        const backBtn =
            e.target.closest("#back-from-detail-btn");
        if (backBtn) {
            hideDetailPage();
            return;
        }
    });

    /**
     * 트레일러 보러가기
     */
    document.addEventListener("click", (e) => {
        const trailerBtn = e.target.closest("#watch-trailer-btn");
        if (trailerBtn) {
            if (!currentDetailMovie?.trailerKey) {
                alert("트레일러가 없습니다.");
                return;
            }

            renderTrailerPage(currentDetailMovie);
            showTrailerPage();
            return;
        }
    });

    /**
     * 상세페이지 복귀
     */
    document.getElementById("back-to-detail-btn")
        ?.addEventListener("click", () => {
            hideTrailerPage();
            showDetailPage();
        });

    /**
     * 로고 → 메인 이동
    */
    document.getElementById("nav-home").addEventListener("click", () => {
        goMainPage();
    });

    const sidebar = document.getElementById("mySidebar");
    const openBtn = document.getElementById("open-sidebar");
    const closeBtn = document.getElementById("close-sidebar");

    console.log("사이드바 요소:", sidebar);
    console.log("열기 버튼:", openBtn);
   
/* 1. 사이드바 열기 버튼 클릭 */
    openBtn?.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation(); // 템플릿 메인 스크립트가 클릭 가로채는 것 방지
        console.log("햄버거 버튼 클릭됨! active 클래스 추가합니다.");
        sidebar.classList.add("active");
    });

    /* 2. 사이드바 닫기 버튼 클릭 */
    closeBtn?.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        sidebar.classList.remove("active");
    });

    /* 3. 메뉴 링크 클릭 시 페이지 이동 후 닫기 */
    document.querySelectorAll("[data-nav]").forEach(link => {
        link.addEventListener("click", (e) => {
            sidebar.classList.remove("active");
            
            // 원래 짜두신 라우팅 로직 실행
            const target = link.dataset.nav;
            if (target === "main") goMainPage();
            if (target === "input") openModal();
            if (target === "bookmark") showBookmarkPage();
        });
    });

    /* 4. 바깥 영역 클릭 시 자동으로 닫히게 처리 */
    document.addEventListener("click", (e) => {
        if (sidebar && sidebar.classList.contains("active")) {
            // 클릭한 곳이 사이드바 내부도 아니고, 열기 버튼도 아니라면 닫기
            if (!sidebar.contains(e.target) && !openBtn.contains(e.target)) {
                sidebar.classList.remove("active");
            }
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

/**
 * 모달 수동 닫기
 */
function initModalClose() {
    document.querySelectorAll("[data-close-modal]").forEach((el) => {
        el.addEventListener("click", closeModal);
    });
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && modalRoot && !modalRoot.hidden) {
            closeModal();
        }
    });
}

/**
 * 영화 상세 페이지 열기
 */
async function openMovieDetail(movieId) {
    try {
        const detail = await getMovieDetail({ id: movieId });
        currentDetailMovie = detail;
        renderDetailPage(detail);
        showDetailPage();
    } catch (error) {
        console.error(error);
        alert("상세 정보를 불러오지 못했습니다.");
    }
}

/**
 * 메인 복귀 함수
 */
function goMainPage() {
    document.getElementById("main").classList.remove("hidden");
    document.getElementById("result-section").classList.add("hidden");
    document.getElementById("page-detail").classList.add("hidden");
    document.getElementById("page-trailer").classList.add("hidden");
    document.getElementById("page-bookmark").classList.add("hidden");
}

/**
 * 북마크 페이지
 */
function showBookmarkPage() {
    document.getElementById("main").classList.add("hidden");
    document.getElementById("result-section").classList.add("hidden");
    document.getElementById("page-detail").classList.add("hidden");
    document.getElementById("page-trailer").classList.add("hidden");

    document.getElementById("page-bookmark").classList.remove("hidden");
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
