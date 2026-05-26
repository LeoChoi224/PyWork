/**
 * 화면 렌더링 및 UI 출력 처리
 */

/**
 * 텍스트를 타이핑 애니메이션처럼 천천히 출력
 */
async function typeText(element, text, speed = 30) {
    element.innerHTML = "";

    for (let i = 0; i < text.length; i++) {
        element.innerHTML += text[i];
        await new Promise(resolve =>
            setTimeout(resolve, speed)
        );
    }
} // end typeText()

/**
 * 결과 페이지 표시
 */
function showResultSection() {
    // 메인 숨기기
    document
        .getElementById("main")
        .classList.add("hidden");

    // 시작 버튼 숨기기
    document
        .getElementById("start-btn")
        .classList.add("hidden");

    // 결과 표시
    document
        .getElementById("result-section")
        .classList.remove("hidden");
} // end showResultSection()

/**
 * 로딩 UI 출력
 */
function renderLoading(message = "로딩 중...") {
    const loadingContainer =
        document.getElementById("loading-container");

    // 기존 입력 영역 숨김
    const titleEl = document.getElementById("modal-title");
    if (titleEl) {
        titleEl.textContent = "AI 추천 결과";
    }
    document.getElementById("user-form").style.display = "none";

    loadingContainer.innerHTML = `
            <div class="loading-box">
                <i class="fas fa-spinner fa-spin"></i>
                ${message}
            </div>
    `;
    loadingContainer.classList.add("loading");
} // end renderLoading()

/**
 * 로딩 제거
 */
function clearLoading() {
    document
        .getElementById("loading-container")
        .classList.remove("loading");
} // end clearLoading()

/**
 * 에러 출력
 */
function renderError(message) {
    const loadingContainer =
        document.getElementById("loading-container");
    if (!loadingContainer) {
        console.error(message);
        return;
    }
    loadingContainer.innerHTML = `
        <p style="color:red;">
            ${message}
        </p>
    `;
} // end renderError()

/**
 * 영화 카드 렌더링
 */
function renderMovieCards(movieList, displayText) {
    const container =
        document.getElementById("movie-output");
    let html = [];
    html.push(displayText);
    for (const item of movieList) {
        const movie = item.movie;
        html.push(`
            <article class="movie-card">
                <img
                    src="${buildPosterUrl(movie.poster_path)}"
                    alt="${movie.title}"
                >
                <h3>${movie.title}</h3>
                <p>${item.ai_reason}</p>
            </article>
        `);
    }
    container.innerHTML = html.join('\n');
} // end renderMovieCards()

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
 * 초기 메인 화면 영화 포스터 목록 렌더링
 */
function renderPosterGrid(movieList) {
    const topContainer = document.getElementById("poster-grid-top");
    const bottomContainer = document.getElementById("poster-grid-bottom");

    // topContainer.innerHTML = "";
    // bottomContainer.innerHTML = "";

    // 첫 줄 8개
    const topMovies = movieList.slice(0, 8);
    // 둘째 줄 9개
    const bottomMovies = movieList.slice(8, 17);

    // 첫 줄 렌더링
    topMovies.forEach((movie) => {
        topContainer.innerHTML += `
            <article class="item thumb span-1">
                <a href="${buildPosterUrl(movie.poster_path, "original")}" class="image">
                    <img src="${buildPosterUrl(movie.poster_path, "w342")}" alt="${movie.title}">
                </a>
            </article>
        `;
    });

    // 둘째 줄 렌더링
    bottomMovies.forEach((movie) => {
        bottomContainer.innerHTML += `
            <article class="item thumb span-1">
                <a href="${buildPosterUrl(movie.poster_path, "original")}" class="image">
                    <img src="${buildPosterUrl(movie.poster_path, "w342")}" alt="${movie.title}">
                </a>
            </article>
        `;
    });
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

