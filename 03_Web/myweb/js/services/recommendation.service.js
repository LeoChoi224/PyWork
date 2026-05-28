/**
 * 추천 시스템 전체 흐름 제어 API
 */

/**
 * 에러 출력
 */
function showFlowError(message) {
    const el = document.getElementById("loading-container")
        || document.getElementById("movie-output");
    if (el) {
        el.innerHTML = `<p style="color:red;">${message}</p>`;
    }
    console.error(message);
}

/**
 * AI 응답에서 JSON 텍스트만 추출
 */
function extractAiText(data) {
    if (typeof data === "string") return data;
    return data?.candidates?.[0]?.content?.parts?.[0]?.text
        ?? data?.choices?.[0]?.message?.content
        ?? null;
}

/**
 * AI 응답 문자열 → JSON 객체 (```json ... ``` 제거)
 */
function parseAiJson(rawText) {
    if (!rawText || typeof rawText !== "string") {
        throw new Error("AI 응답이 비어 있습니다.");
    }
    let text = rawText.trim();
    // ```json ... ``` 또는 ``` ... ``` 제거
    const fenced = text.match(/^```(?:json)?\s*([\s\S]*?)\s*```$/i);
    if (fenced) {
        text = fenced[1].trim();
    } else {
        text = text.replace(/^```(?:json)?\s*/i, "").replace(/\s*```$/i, "").trim();
    }
    return JSON.parse(text);
}

/**
 * 1단계: 사용자 분석 + 태그 (UI 없음)
 */
async function analyzeUserTags(userInfo) {
    const promptInput = PROMPTS.analyzeUser(userInfo);
    console.log(promptInput);

    const data = CONFIG.AI_PROVIDER == "openai"
        ? await callOpenAi(promptInput)
        : await callGemini(promptInput);

    if (!data) return null;

    const rawText = extractAiText(data);
    if (!rawText) throw new Error("AI 분석 응답이 비어 있습니다.");

    return parseAiJson(rawText);
}

/**
 * 2단계: TMDB 후보 (UI 없음)
 */
async function fetchMovieCandidates(aiTagsObject) {
    const keywordIds = await getKeywordIdFromTMDB(aiTagsObject);
    const genreIds = aiTagsObject.genres
        .map((name) => GENRES[name])
        .filter((id) => id != null);
    console.log(`TMDB 검색에 사용할 장르: [${aiTagsObject.genres[0]}=${genreIds[0]}, ${aiTagsObject.genres[1]}=${genreIds[1]}]`);

    const classicUrl = buildClassicMovieUrl(genreIds, keywordIds);
    const recentUrl = buildRecentMovieUrl(genreIds, keywordIds);
    const [classicCandidates, recentCandidates] = await Promise.all([
        getCandidatesFromTMDB(aiTagsObject, classicUrl),
        getCandidatesFromTMDB(aiTagsObject, recentUrl),
    ]);
    return { classicCandidates, recentCandidates, genreIds, keywordIds };
}

/**
 * 3단계: 최종 3편 + 상세 (UI 없음 — renderMovieCards 제거한 버전)
 */
async function pickFinalMovies(userInfo, aiTagsObject, classicCandidates, recentCandidates) {
    const promptInput = PROMPTS.recommendMovie(
        userInfo,
        aiTagsObject,
        classicCandidates,
        recentCandidates
    );

    const data = CONFIG.AI_PROVIDER == "openai"
        ? await callOpenAi(promptInput)
        : await callGemini(promptInput);

    if (!data) return null;

    const rawText = extractAiText(data);
    if (!rawText) throw new Error("최종 추천 응답이 비어 있습니다.");

    const recommendationResult = parseAiJson(rawText);
    const detailedRecommendations = [];
    for (const movie of recommendationResult.recommendations) {
        const detail = await getMovieDetail(movie);
        if (detail) {
            detailedRecommendations.push({
                movie: detail,
                ai_reason: movie.reason,
            });
        }
    }
    return detailedRecommendations;
}
/**
 * 전체 흐름 제어
 */
async function runRecommendationFlow() {
    const userInfo = getUserInput();
    
    try {
        // 1) AI 분석
        const aiTagsObject = await analyzeUserTags(userInfo);
        if (!aiTagsObject) {
            return { ok: false, message: "AI 분석에 실패했습니다." };
        }
        console.log("AI 분석 및 추천 답변 텍스트:\n", aiTagsObject);
        clearLoading();

        // 2) 화면 타이핑(병렬)
        const displayText = formatAnalysisText(aiTagsObject);
        const loadingContainer = document.getElementById("loading-container");
        const typingPromise = typeText(loadingContainer, displayText, 30);

        // 3) TMDB + 최종 추천은 await로 진행
        const recommendationsPromise = (async () => {
            const { classicCandidates, recentCandidates } =
                await fetchMovieCandidates(aiTagsObject);
            return await pickFinalMovies(
                userInfo, aiTagsObject, classicCandidates, recentCandidates
            );
        })();

        // 4) 둘 다 완료될 때까지 대기
        const [, recommendations] = await Promise.all([typingPromise, recommendationsPromise]);

        // 타이핑 끝난 후 1초 대기 추가
        await new Promise(resolve => setTimeout(resolve, 1000));

        if (!recommendations?.length) {
            return { ok: false, message: "추천 결과가 없습니다." };
        }

        return {
            ok: true,
            userInfo,
            aiTagsObject,
            displayText,
            recommendations
        };

    } catch (error) {
        console.error(error);
        showFlowError(`오류 발생: ${error.message}`);
        return { ok: false, message: error.message || "알 수 없는 오류" };
    }
}