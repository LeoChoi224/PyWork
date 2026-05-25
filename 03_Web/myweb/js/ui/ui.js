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
 * 특정 페이지 표시
 */
function showPage(pageId) {
    document
        .querySelectorAll(".view")
        .forEach(page => {
            page.classList.remove("active");
            page.classList.add("hidden");
        });
    const targetPage =
        document.getElementById(pageId);
    targetPage.classList.remove("hidden");
    targetPage.classList.add("active");
} // end showPage()

/**
 * 로딩 UI 출력
 */
function renderLoading(message = "로딩 중...") {
    const output =
        document.getElementById("analysis-output");
    output.innerHTML = `
        <i class="fas fa-spinner fa-spin"></i>
        ${message}
    `;
    output.classList.add("loading");
} // end renderLoading()

/**
 * 로딩 제거
 */
function clearLoading() {
    document
        .getElementById("analysis-output")
        .classList.remove("loading");
} // end clearLoading()

/**
 * 에러 출력
 */
function renderError(message) {
    const output =
        document.getElementById("analysis-output");
    output.innerHTML = `
        <span style="color:red;">
            ${message}
        </span>
    `;
} // end renderError()

/**
 * AI 분석 결과 출력
 */
async function renderAnalysis(aiTagsObject) {
    const output =
        document.getElementById("analysis-output");
    const displayText =
        formatAnalysisText(aiTagsObject);

    console.log("사용자에게 보여줄 텍스트", displayText);
    typeText(output, displayText, 70);
} // end renderAnalysis()

/**
 * 영화 카드 렌더링
 */
function renderMovieCards(movieList) {
    const container =
        document.getElementById("movie-output");
    let html = [];
    for (const item of movieList) {
        const movie = item.movie;
        html.push(`
            <div class="movie-card">
                <img
                    src="${buildPosterUrl(movie.poster_path)}"
                    alt="${movie.title}"
                >
                <h3>${movie.title}</h3>
                <p>${item.ai_reason}</p>
            </div>
        `);
    }
    container.innerHTML = html.join('\n');
} // end renderMovieCards()

/**
 * 결과 화면 초기화
 */
function clearResult() {
    document.getElementById("analysis-output").innerHTML = "";
    document.getElementById("movie-output").innerHTML = "";
} // end clearResult()

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

