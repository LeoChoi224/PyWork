/**
 * 화면 이동 라우팅 및 이벤트 처리
 */

document.addEventListener("DOMContentLoaded", () => {
    // 첫 화면 고정
    showPage("page-main");
    
    // 시작 버튼
    const startBtn = document
        .getElementById("start-btn");
    
    console.log(startBtn);
    startBtn.addEventListener("click", () => {
        showPage("page-input");
    });
    
    
    // 추천 받기 버튼
    const recommendBtn =
        document.getElementById("recommend-btn");
    
    console.log(recommendBtn);
    recommendBtn
        .addEventListener("click", async () => {
            showPage("page-loading");
            await getSearchTagsFromAI();
            showPage("page-result");
        });
});

// document
//     .getElementById("restart-btn")
//     .addEventListener("click", resetApp);

// document
//     .getElementById("back-to-result-btn")
//     .addEventListener("click", showResultPage);