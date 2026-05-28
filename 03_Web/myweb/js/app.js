/**
 * 화면 이동 라우팅 및 이벤트 처리
 */

/**
 * 현재 상세 영화
 */
let currentDetailMovie = null;
let previousPage = "main";

document.addEventListener("DOMContentLoaded", () => {

    // 1. 초기 로드 시 메인 페이지 동적 그리드 계산해서 출력 (기본값+북마크 연동)
    const initialMovies = BookmarkManager.getMainGridMovies();
    renderPosterGrid(initialMovies);

    /**
     * 네비게이션 좌측 사이드바 컨트롤 이벤트
     */
    const sidebar = document.getElementById("mySidebar");
    const openBtn = document.getElementById("open-sidebar");
    const closeBtn = document.getElementById("close-sidebar");
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
    /* 3. 네비바 메뉴 클릭 시 라우팅 분기 처리 */
    document.addEventListener("click", (e) => {
        const link = e.target.closest("[data-nav]");
        if (!link) return;

        sidebar?.classList.remove("active"); // 메뉴 선택 시 서랍 자동 닫기
        const target = link.dataset.nav;

        if (target === "main") {
            // 메인 복귀 시 북마크 변동사항 즉시 밀어내기 반영을 위해 리렌더링 실행
            renderPosterGrid(BookmarkManager.getMainGridMovies());
            document.getElementById("page-bookmark")?.classList.add("hidden");
            document.getElementById("result-section")?.classList.add("hidden");
            document.getElementById("page-detail")?.classList.add("hidden");
            document.getElementById("main")?.classList.remove("hidden");
            document.getElementById("start-btn")?.classList.remove("hidden");
        } else if (target === "input") {
            // 정보입력 전용 처리 함수 호출 (예: openModal 등 모달 시스템 매칭)
            if (typeof openModal === "function") openModal();
        } else if (target === "bookmark") {
            showBookmarkPage();
        }
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

    initModalClose();

    // 헤더 뒤로가기 버튼
    document.getElementById("global-back-btn")?.addEventListener("click", goBack);

    // 시작 버튼
    const startBtn = document.getElementById("start-btn");
    console.log(startBtn);

    // 시작 버튼 -> 모달 열기
    startBtn?.addEventListener("click", openModal);

    // 추천 받기 버튼
    const recommendBtn = document.getElementById("recommend-btn");
    console.log(recommendBtn);

    // 입력 폼 내부 키 이벤트 전파 차단
    document.querySelectorAll("#user-form input, #user-form textarea, #user-form select")
        .forEach((el) => {
            el.addEventListener("keydown", (e) => {
                e.stopPropagation();
            });

            el.addEventListener("keyup", (e) => {
                e.stopPropagation();
            });
        });

    recommendBtn.addEventListener("click", async (e) => {
        e.preventDefault();

        // 유효성 검증 먼저
        const validateUser = getUserInput();
        // 검증 실패 시 즉시 종료
        if (!validateUser) { return; }

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

    // 메인 포스터 클릭 이벤트
    document.addEventListener("click", async (e) => {
        const posterLink = e.target.closest(".item.thumb .image");
        if (!posterLink) return;

        // 템플릿 기본 gallery 막기
        e.preventDefault();
        e.stopPropagation();

        const poster = e.target.closest(".item.thumb");
        document.getElementById("start-btn")?.classList.add("hidden");

        const movieId = poster.dataset.movieId;
        if (!movieId) return;

        previousPage = "main";

        await openMovieDetail(movieId);
    });

    // 추천 결과 카드 클릭 이벤트
    document.addEventListener("click", async (e) => {
        const movieCard = e.target.closest(".movie-card:not(.bookmark-card)");
        if (!movieCard) return;

        previousPage = "result";

        const movieId = movieCard.dataset.movieId;
        if (!movieId) return;

        await openMovieDetail(movieId);
    });

    // 북마크 카드 클릭 이벤트
    document.addEventListener("click", async (e) => {
        const bookmarkCard = e.target.closest(".bookmark-card");
        if (!bookmarkCard) return;

        previousPage = "bookmark";

        const movieId = bookmarkCard.dataset.movieId;
        if (!movieId) return;

        await openMovieDetail(movieId);
    });

    document.addEventListener("keydown", (e) => {
        if (e.key !== "Escape") return;

        const detailPage = document.getElementById("page-detail");

        if (detailPage && !detailPage.classList.contains("hidden")) {
            goBack();
        }
    });

    /**
     * 상세 페이지 버튼 이벤트
     */
    document.addEventListener("click", (e) => {
        /**
         * 추천 목록으로 가기
         */
        const backBtn = e.target.closest("#back-from-detail-btn");
        if (backBtn) {
            goBack();
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

    /**
    * 북마크 토글
    */
    document.addEventListener("click", (e) => {
        const bookmarkBtn = e.target.closest(".bookmark-btn");
        if (!bookmarkBtn) return;
        if (!currentDetailMovie) return;

        // 토글 실행
        const isBookmarked = BookmarkManager.toggle(currentDetailMovie);

        // 버튼 상태 즉시 변경
        if (isBookmarked) {
            bookmarkBtn.className = "fa-solid fa-star bookmarked bookmark-btn active";
            bookmarkBtn.innerHTML = "북마크 해제";

        } else {
            bookmarkBtn.className = "fa-regular fa-star bookmark-btn";
            bookmarkBtn.innerHTML = "북마크 하기";
        }

        // 메인 포스터 즉시 반영
        renderPosterGrid(BookmarkManager.getMainGridMovies());
        // 북마크 페이지 열려있다면 즉시 갱신
        renderBookmarkPage();
    });

    /**
     * 북마크 전체 삭제
     */
    document.getElementById("clear-bookmark-btn")?.addEventListener("click", () => {
        const ok = confirm("북마크를 모두 삭제하시겠습니까?");
        if (!ok) return;

        BookmarkManager.clearAll();

        renderBookmarkPage();
        renderPosterGrid(BookmarkManager.getMainGridMovies());
    });


});

const body = document.body; // body 요소
const modalRoot = document.getElementById("modal-root"); // 모달 최상위 컨테이너
const navOpenForm = document.getElementById("nav-open-form"); // 네비 '취향 입력' 링크
/**
 * 모달 열기
 */
function openModal() {
    resetRecommendationModal(); // 추천 결과 상태 초기화
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
    document.getElementById("start-btn").classList.remove("hidden");
    document.getElementById("main").classList.remove("hidden");
    document.getElementById("result-section").classList.add("hidden");
    document.getElementById("page-detail").classList.add("hidden");
    document.getElementById("page-trailer").classList.add("hidden");
    document.getElementById("page-bookmark").classList.add("hidden");
    // 북마크 반영 재렌더
    renderPosterGrid(BookmarkManager.getMainGridMovies());
    updateBackButton();
}

/**
 * 북마크 페이지
 */
function showBookmarkPage() {
    document.getElementById("main").classList.add("hidden");
    document.getElementById("result-section").classList.add("hidden");
    document.getElementById("page-detail").classList.add("hidden");
    document.getElementById("page-trailer").classList.add("hidden");
    document.getElementById("start-btn").classList.add("hidden");

    document.getElementById("page-bookmark").classList.remove("hidden");

    // 북마크 목록 렌더링
    renderBookmarkPage();
    updateBackButton();
}

/**
 * 이전 페이지 복귀
 */
function goBack() {

    // 전부 숨김
    document.getElementById("main")?.classList.add("hidden");
    document.getElementById("result-section")?.classList.add("hidden");
    document.getElementById("page-detail")?.classList.add("hidden");
    document.getElementById("page-bookmark")?.classList.add("hidden");
    document.getElementById("page-trailer")?.classList.add("hidden");

    // 이전 페이지 복귀
    if (previousPage === "main") {

        document.getElementById("main")?.classList.remove("hidden");
        document.getElementById("start-btn")?.classList.remove("hidden");

    } else if (previousPage === "result") {

        document.getElementById("result-section")?.classList.remove("hidden");

    } else if (previousPage === "bookmark") {

        document.getElementById("page-bookmark")?.classList.remove("hidden");
    }
    updateBackButton();
}

/**
 * 헤더 뒤로가기 버튼 표시 여부
 */
function updateBackButton() {

    const backBtn = document.getElementById("global-back-btn");

    if (!backBtn) return;

    const isMainVisible =
        !document.getElementById("main")?.classList.contains("hidden");

    if (isMainVisible) {
        backBtn.classList.add("hidden");
    } else {
        backBtn.classList.remove("hidden");
    }
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
