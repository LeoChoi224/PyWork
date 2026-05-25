/**
 * 추천 시스템 전체 흐름 제어 API
 */

/**
 * AI에게 사용자 정보를 보내 분석을 받고, 실시간 화면 표시 후 태그 객체 리턴
*/
async function getSearchTagsFromAI() {
    console.log("1. 사용자 정보 분석 및 태그 추출 시작");

    const userInfo = await getUserInput();
    if (!userInfo) return null; // 유효성 검사 실패 시 중단

    const promptInput = PROMPTS.analyzeUser(userInfo);
    console.log(promptInput);

    await renderLoading("응답 생성 중... 잠시 기다려주십시오.");

    try {
        // 요청 본문
        const data = await callGemini(promptInput);
        // const data = await callOpenAi(promptInput);

        await clearLoading();
        // 응답 텍스트 추출
        const rawText =
            data.candidates?.[0]?.content?.parts?.[0]?.text;
        console.log("AI 분석 및 추천 답변 텍스트:\n", rawText);

        // JSON 파싱
        const aiTagsObject = JSON.parse(rawText);
        console.log("성공적으로 생성된 자바스크립트 오브젝트:", aiTagsObject);

        renderAnalysis(aiTagsObject);

        // 키워드, 장르 ID 추출
        const keywordIds = await getKeywordIdFromTMDB(aiTagsObject);
        const genreIds = [];
        aiTagsObject.genres.forEach(genres => genreIds.push(GENRES[genres]))
        console.log(`TMDB 검색에 사용할 장르: [${aiTagsObject.genres[0]}=${genreIds[0]}, ${aiTagsObject.genres[1]}=${genreIds[1]}]`);

        // 최근 영화 조건을 미포함 시켜 명작 기준으로 추천받기 위함
        const classicCandidates =
            await getCandidatesFromTMDB(
                aiTagsObject,
                await buildClassicMovieUrl(
                    genreIds,
                    keywordIds
                )
            );
        // 최근 영화 조건을 포함 시켜 최신 기준으로 추천받기 위함
        const recentCandidates =
            await getCandidatesFromTMDB(
                aiTagsObject,
                await buildRecentMovieUrl(
                    genreIds,
                    keywordIds
                )
            );

        const fianl = await getFinalRecommendations(userInfo, aiTagsObject, classicCandidates, recentCandidates);
        console.log("최종 결과", fianl);

        return aiTagsObject;

    } catch (error) {
        console.error("Fetch 또는 스트림 처리 중 오류 발생:", error);
        outputElement.textContent = `오류 발생: ${error.message}`;
        return null;
    }
} // end streamGeminiResponse()

/**
 * 후보군 리스트와 사용자 정보를 다시 OpenAI에 보내어 최종 3개를 고르고 이유를 작성받음
*/
async function getFinalRecommendations(inputData, aiTagsObject, classicCandidates, recentCandidates) {
    console.log("4. 최종 3개 영화를 추천 요청");

    if (!inputData) return null; // 유효성 검사 실패 시 중단

    const outputElement = document.getElementById('movie-output');

    const promptInput = PROMPTS.recommendMovie(inputData, aiTagsObject, classicCandidates, recentCandidates);
    console.log(promptInput);

    try {
        const data = await callGemini(promptInput);
        // const data = await callOpenAi(promptInput);

        // 응답 텍스트 추출
        const rawText =
            data.candidates?.[0]?.content?.parts?.[0]?.text;
        console.log("AI 최종 답변 텍스트:\n", rawText);

        // JSON 파싱
        const recommendationResult = JSON.parse(rawText);
        console.log("최종 추천 영화 3개 자바스크립트 오브젝트:", recommendationResult);

        const detailedRecommendations = [];
        for (const movie of recommendationResult.recommendations) {
            const detail = await getMovieDetail(movie);
            detailedRecommendations.push({
                movie: detail,
                ai_reason: movie.reason
            });
        }

        console.log(detailedRecommendations);
        await renderMovieCards(detailedRecommendations);

        return detailedRecommendations;

    } catch (error) {
        console.error("Fetch 또는 스트림 처리 중 오류 발생:", error);
        outputElement.textContent = `오류 발생: ${error.message}`;
        return null;
    }
}

/**
 * 전체 흐름을 제어하는 메인 API 함수
 */
async function runRecommendationFlow(userInfo) {
    // const tags = await getSearchTagsFromAI(userInfo);
    // const candidates = await getCandidatesFromTMDB(tags);
    // const finalPicks = await getFinalRecommendations(userInfo, candidates);

    // return { candidates, finalPicks }; // app.js로 데이터 전달
}

