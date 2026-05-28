/**
 * 화면 렌더링 및 UI 출력 처리
 */

/**
 * 텍스트를 타이핑 애니메이션처럼 천천히 출력
 */
async function typeText(element, text, speed = 30) {
    if (!element) return;
    element.innerHTML = "";
    const plain = String(text ?? "").replace(/\r\n/g, "\n");

    for (let i = 0; i < plain.length; i++) {
        const ch = plain[i];
        element.innerHTML += (ch === "\n") ? "<br>" : ch;
        await new Promise((resolve) => setTimeout(resolve, speed));
    }
} // end typeText()

/**
 * 결과 페이지 표시
 */
function showResultSection() {
    // 메인 숨기기
    document.getElementById("main").classList.add("hidden");
    // 시작 버튼 숨기기
    document.getElementById("start-btn").classList.add("hidden");
    // 결과 표시
    document.getElementById("result-section").classList.remove("hidden");
    updateBackButton();
} // end showResultSection()

/**
 * 로딩 UI 출력
 */
function renderLoading(message = "로딩 중...") {
    const loadingContainer = document.getElementById("loading-container");

    // 기존 입력 영역 숨김
    const titleEl = document.getElementById("modal-title");
    if (titleEl) {
        titleEl.textContent = "AI 추천 결과";
    }
    const userForm = document.getElementById("user-form");
    if (userForm) userForm.style.display = "none";

    if (loadingContainer) {
        loadingContainer.innerHTML = `
            <div class="loading-box">
                <i class="fas fa-spinner fa-spin"></i>
                ${message}
            </div>
    `;
        loadingContainer.classList.add("loading");
    }
} // end renderLoading()

/**
 * 로딩 제거
 */
function clearLoading() {
    document.getElementById("loading-container").classList.remove("loading");
} // end clearLoading()

/**
 * 에러 출력
 */
function renderError(message) {
    const loadingContainer = document.getElementById("loading-container");
    if (!loadingContainer) {
        console.error(message);
        return;
    }
    loadingContainer.innerHTML = `<p style="color:red;">${message}</p>`;
} // end renderError()

/**
 * 결과 화면 초기화
 */
function clearResult() {
    const analysis = document.getElementById("loading-container");
    const movie = document.getElementById("movie-output");
    if (analysis) analysis.innerHTML = "";
    if (movie) movie.innerHTML = "";
} // end clearResult()

/**
 * 상세 페이지 표시
 */
function showDetailPage() {
    // 기존 페이지 숨김
    document.getElementById("main")?.classList.add("hidden");
    document.getElementById("result-section")?.classList.add("hidden");
    document.getElementById("page-bookmark")?.classList.add("hidden");
    // 상세 페이지 표시
    document.getElementById("page-detail")?.classList.remove("hidden");
    updateBackButton();
}
/**
 * 상세 페이지 숨기기
 */
function hideDetailPage() {
    // 상세 페이지 숨김
    document.getElementById("page-detail")?.classList.add("hidden");
    // 결과 페이지 복귀
    document.getElementById("result-section")?.classList.remove("hidden");
}

/**
 * 트레일러 페이지 렌더링
 */
function renderTrailerPage(movie) {
    const container = document.getElementById("trailer-container");
    if (!container) return;

    container.innerHTML = `
        <div class="trailer-layout">
            <iframe class="trailer-frame"
                src="https://www.youtube.com/embed/${movie.trailerKey}"
                title="${movie.title}" allowfullscreen>
            </iframe>
           
        </div>
    `;
}

/**
 * 트레일러 페이지 표시
 */
function showTrailerPage() {
    // 결과 페이지 숨김
    document.getElementById("page-detail")?.classList.add("hidden");
    // 트레일러 페이지 표시
    document.getElementById("page-trailer")?.classList.remove("hidden");
    updateBackButton();
}
/**
 * 트레일러 페이지 숨기기
 */
function hideTrailerPage() {
    // 트레일러 페이지 숨김
    document.getElementById("page-trailer")?.classList.add("hidden");
    // 결과 페이지 복귀
    document.getElementById("page-detail")?.classList.remove("hidden");
    updateBackButton();
}

/**
 * 추천 모달 상태 초기화
 */
function resetRecommendationModal() {
    // 제목 복구
    const titleEl = document.getElementById("modal-title");

    if (titleEl) { titleEl.textContent = "영화 취향 입력"; }

    // 폼 다시 표시
    const userForm = document.getElementById("user-form");

    if (userForm) { userForm.style.display = "block"; }

    // 로딩 제거
    const loadingContainer = document.getElementById("loading-container");

    if (loadingContainer) {
        loadingContainer.innerHTML = "";
        loadingContainer.classList.remove("loading");
    }
}

/**
 * 개발 단계에서 확인용으로 화면에 뿌리기
 */
function renderMoviePreview(movieList) {
    let table = [];
    table.push("<hr><table><tr><td>영화명</td><td>이미지</td></tr>");

    for (const m of movieList) {
        // 포스터 경로가 있으면 <img> 태그를 만들고, 없으면 '이미지 없음' 글자를 띄웁니다.
        let posterImg = m.movie.poster_path
            ? `<img src="${buildPosterUrl(m.movie.poster_path)}">`
            : "이미지 없음";
        table.push(`
            <tr>
                <td>${m.movie.title}</td>    
                <td>${posterImg}</td>
                <td>${m.ai_reason}</td>
            </tr>
        `);
    }

    table.push("</table>")
    document.getElementById('test-output').innerHTML += table.join('\n');
} //end renderMoviePreview()


/**
 * 초기 메인 화면 영화 포스터 목록 렌더링
 * [수정] 메인 화면 영화 포스터 목록 렌더링 (홀수일 때 바텀이 1개 더 가져가는 동적 확장 구조)
 */
function renderPosterGrid(movieList) {
    const topContainer = document.getElementById("poster-grid-top");
    const bottomContainer = document.getElementById("poster-grid-bottom");

    if (!topContainer || !bottomContainer) return;

    // 기존에 그려져 있던 내용물 싹 비우기
    topContainer.innerHTML = "";
    bottomContainer.innerHTML = "";

    // 8개, 9개씩 쪼개서 담을 행 배열들
    const topRows = [];    // 홀수 번째 줄들 (8개씩)
    const bottomRows = []; // 짝수 번째 줄들 (9개씩)

    const totalCount = movieList.length;

    // [핵심 알고리즘] 전체 개수를 반으로 나누어 상단과 하단 칸수를 동적으로 계산합니다.
    // 홀수일 경우 하단(Bottom)이 1개 더 가져갑니다.
    // 예: 17개 -> topLimit = 8 (Top 8개 / Bottom 9개)
    // 예: 18개 -> topLimit = 9 (Top 9개 / Bottom 9개)
    // 예: 19개 -> topLimit = 9 (Top 9개 / Bottom 10개)
    const topLimit = Math.floor(totalCount / 2);

    // 1. 윗줄(Top Line)에 배치될 영화 조각
    const topMovies = movieList.slice(0, topLimit);
    // 2. 아랫줄(Bottom Line)에 배치될 영화 조각
    const bottomMovies = movieList.slice(topLimit);

    // 상단(Top) 라인 출력
    topContainer.innerHTML += `
        <div class="item intro span-2">
            <h1>롯데시네묵</h1>
            <p>나이, MBTI, 오늘의 기분에 맞는<br />
                당신만을 위한 영화를 찾아드립니다.</p>
        </div>
    `
    topMovies.forEach((movie) => {
        topContainer.innerHTML += `
               <article class="item thumb span-1" data-movie-id="${movie.id}">
                   <a href="${buildPosterUrl(movie.poster_path, "original")}" class="image">
                       <img src="${buildPosterUrl(movie.poster_path, "w342")}" alt="${movie.title}">
                   </a>
               </article>
           `;
    });

    // 하단(Bottom) 라인 출력
    bottomMovies.forEach((movie) => {
        bottomContainer.innerHTML += `
               <article class="item thumb span-1" data-movie-id="${movie.id}">
                   <a href="${buildPosterUrl(movie.poster_path, "original")}" class="image">
                       <img src="${buildPosterUrl(movie.poster_path, "w342")}" alt="${movie.title}">
                   </a>
               </article>
           `;
    });
}

/**
 * 영화 카드 렌더링
 * [수정] 결과 페이지 영화 카드 렌더링 (북마크 별 아이콘 상태 연동)
 */
function renderMovieCards(movieList, displayText) {
    const container = document.getElementById("movie-output");
    if (!container) return;

    let html = [];
    html.push(displayText);

    for (const item of movieList) {
        const movie = item.movie;

        html.push(`
            <article class="movie-card"
                data-movie-id="${movie.id}">
                <img src="${buildPosterUrl(movie.poster_path)}" alt="${movie.title}">
                <h3>${movie.title}</h3>
                <p>${item.ai_reason}</p>
            </article>
        `);
    }
    container.innerHTML = html.join('\n');
} // end renderMovieCards()

/**
 * 상세 페이지 렌더링
 * [수정] 상세 페이지 렌더링 내부에 북마크 초기 상태값 반영하도록 보완
 */
function renderDetailPage(movie) {
    const container = document.getElementById("detail-container");
    if (!container) return;

    const releaseYear = movie.release_date?.split("-")[0] || "-";
    const runtimeHour = Math.floor(movie.runtime / 60);
    const runtimeMinute = movie.runtime % 60;

    // 현재 북마크 상태에 따른 클래스 및 텍스트 분기
    const isBookmarked = BookmarkManager.isBookmarked(movie.id);
    const btnText = isBookmarked ? "북마크 해제" : "북마크 하기";
    const btnClass = isBookmarked ? "fa-solid fa-star bookmarked bookmark-btn active" : "fa-regular fa-star bookmark-btn";

    container.innerHTML = `
        <div class="detail-layout" style="--backdrop-url: url('https://image.tmdb.org/t/p/original${movie.backdrop_path}')">
            <section class="detail-left">
                <img class="detail-poster" src="${buildPosterUrl(movie.poster_path, "w500")}" alt="${movie.title}">
            </section>
            <section class="detail-right">
                <div class="detail-top">
                    <h1 class="detail-title">${movie.title}</h1>
                    <button
                        class="${btnClass}"
                        data-bookmark-id="${movie.id}"
                        style="visibility:hidden"
                    >
                        ${btnText}
                    </button>
                </div>
                <div class="detail-meta">
                    ${releaseYear} · ⭐ ${movie.vote_average.toFixed(1)} · ${runtimeHour}시간 ${runtimeMinute}분
                </div>
                <div class="detail-info-grid">
                    <div class="detail-label">감독</div>
                    <div class="detail-value">${movie.director}</div>
                    <div class="detail-label">배우</div>
                    <div class="detail-value">${movie.cast.join(", ")}</div>
                    <div class="detail-label">장르</div>
                    <div class="detail-value">${movie.genres.map(g => g.name).join(", ")}</div>
                    <div class="detail-label">줄거리</div>
                    <div class="detail-value detail-overview">${movie.overview}</div>
                </div>
                <div class="detail-bottom-buttons">
                    <button class="button primary" id="watch-trailer-btn" data-trailer-key="${movie.trailerKey || ""}">
                        🎬 트레일러 보러가기
                    </button>
<button type="button" id="back-from-detail-btn" class="button">

    ← 뒤로가기

</button>
                </div>
            </section>
        </div>
    `;

    requestAnimationFrame(() => {
        const bookmarkBtn = container.querySelector(".bookmark-btn");

        if (bookmarkBtn) {
            bookmarkBtn.style.visibility = "visible";
        }
    });
}

/**
 * 북마크 페이지 렌더링
 */
function renderBookmarkPage() {
    const container = document.getElementById("bookmark-container");
    if (!container) return;

    const bookmarks = BookmarkManager.getAll();

    // 비어있을 경우
    if (bookmarks.length === 0) {
        container.innerHTML = `
            <div class="empty-bookmark">
                <h2>북마크한 영화가 없습니다.</h2>
                <p>마음에 드는 영화를 저장해보세요.</p>
            </div>
        `;
        return;
    }

    let html = [];
    bookmarks.forEach(movie => {
        html.push(`
            <article class="movie-card bookmark-card"
                data-movie-id="${movie.id}">
                <img src="${buildPosterUrl(movie.poster_path)}"
                    alt="${movie.title}">
                <h3>${movie.title}</h3>
            </article>
        `);
    });
    container.innerHTML = html.join("");
}