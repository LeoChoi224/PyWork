/**
 * OpenAI 및 TMDB API 호출 핵심 로직
 */

/**
 * 사용자 정보 받기 & 검증
 */
function getUserInput() {
    let frm = document.forms.infoForm;
    let mbti = frm.mbti?.value?.trim().toUpperCase() || "";

    // MBTI 유효성 검증
    if (mbti && !/^[EI][SN][TF][JP]$/i.test(mbti)) {
        alert(`"${mbti}"는 유효한 값이 아닙니다. 💢\n MBTI를 입력 하세요. 예: ISTP`);
        frm.mbti.focus();
        return null;
    } else {
        // 프롬프트에 맞춤 리팩터링
        const userInfo = {
            mbti: mbti ? mbti : "미 입력",
            gender: frm.gender.value == "male" ? "남자" : "여자",
            age: frm.age.value ? `${frm.age.value}세` : "미 입력",
            mood: frm.mood.value.trim() ? `${frm.mood.value.trim()}` : "미 입력",
        }
        return userInfo;
    }
} // end getUserInput()

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
}

/**
 * AI에게 사용자 정보를 보내 분석을 받고, 실시간 화면 표시 후 태그 객체 리턴
*/
// Gemini 버전
async function getSearchTagsFromAI() {
    console.log("1. 사용자 정보 분석 및 태그 추출 시작");

    const inputData = getUserInput();
    if (!inputData) return null; // 유효성 검사 실패 시 중단

    const outputElement = document.getElementById('analysis-output');

    const promptInput = PROMPTS.analyzeUser(inputData);
    console.log(promptInput);

    outputElement.innerHTML = "<i class='fas fa-spinner fa-spin'></i>응답 생성 중... 잠시 기다려주십시오."
    outputElement.classList.add('loading');

    // request body (요청 본문)
    const requestBody = {
        contents: [{
            parts: [{ text: promptInput }]
        }],
        generationConfig: {
            responseMimeType: "application/json",
            temperature: 0.7 // 숫자가 작을수록 기계적, 클수록 창의적, 1 이상은 너무 랜덤
        }
    };

    try {
        // 스트리밍 말고 응답 자체는 빨리 완성시킴
        const response = await fetch(CONFIG.GEMINI_API_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();
        outputElement.classList.remove('loading');

        // HTTP 상태 코드 확인
        if (!response.ok) {
            outputElement.innerHTML = `<span style="color: red;">API 요청 실패 (HTTP ${response.status})</span>`;
            return null;
        }

        // Gemini 응답 텍스트 추출
        const rawText =
            data.candidates?.[0]?.content?.parts?.[0]?.text;
        console.log("AI 최종 답변 텍스트:\n", rawText);

        // JSON 파싱
        const aiTagsObject = JSON.parse(rawText);
        console.log("성공적으로 생성된 자바스크립트 오브젝트:", aiTagsObject);

        // 사용자에게 보여줄 텍스트 생성
        const displayText = `
📊 사용자 분석
${aiTagsObject.analysis}
🎬 추천 장르
${aiTagsObject.genres.map(g => g).join(", ")}
🏷 추천 키워드
${aiTagsObject.keywords.map(k => k.ko).join(", ")}
`;

        // 화면은 일부러 천천히 출력
        typeText(outputElement, displayText, 20);

        const keywordIds = await getKeywordIdFromTMDB(aiTagsObject);
        const genreIds = [];
        aiTagsObject.genres.forEach(genres => genreIds.push(GENRES[genres]))
        console.log(`TMDB 검색에 사용할 장르: [${aiTagsObject.genres[0]}=${genreIds[0]}, ${aiTagsObject.genres[1]}=${genreIds[1]}]`);

        // 최근 영화 조건을 미포함 시켜 명작 기준으로 추천받기 위함
        const classicCandidates =
            await getCandidatesFromTMDB(
                aiTagsObject,
                TMDB_CLASSIC_URL(
                    genreIds,
                    keywordIds
                )
            );
        // 최근 영화 조건을 포함 시켜 최신 기준으로 추천받기 위함
        const recentCandidates =
            await getCandidatesFromTMDB(
                aiTagsObject,
                TMDB_RECENT_URL(
                    genreIds,
                    keywordIds
                )
            );
        return aiTagsObject;

    } catch (error) {
        console.error("Fetch 또는 스트림 처리 중 오류 발생:", error);
        outputElement.textContent = `오류 발생: ${error.message}`;
        return null;
    }

} // end streamGeminiResponse()

// OpenAI 버전
// async function getSearchTagsFromAI(userInfo) {
//     console.log("1. 사용자 정보 분석 및 태그 추출 시작");
//     // TODO: OpenAI API 호출 (prompt: 이 사용자의 기분에 맞는 TMDB 장르 ID를 배열로 줘)
//     // Return 예시: { genre_ids: [18, 35], keywords: "sad, healing" }
//     return { genre_ids: [18] };
// }

/**
 * 키워드 Id 가져오기
*/
async function getKeywordIdFromTMDB(aiTagsObject) {
    console.log("2. TMDB API로 키워드 ID 검색");

    if (!aiTagsObject || !aiTagsObject.keywords || aiTagsObject.keywords.length === 0) {
        console.error("전달된 키워드가 없습니다.");
        return [];
    }

    const keywordIds = [];

    for (const keywordObj of aiTagsObject.keywords) {
        const keyword = keywordObj.en;
        const url = `
${CONFIG.TMDB_URL}search/keyword
?query=${encodeURIComponent(keyword)}
&api_key=${CONFIG.TMDB_KEY}
`;
        try {
            const response = await fetch(url);
            const data = await response.json();

            const keywordId = data?.results?.[0]?.id;
            keywordId && keywordIds.push(keywordId);

        } catch (error) {
            console.error("TMDB 호출 오류:", error);
            return [];
        }
    }
    return keywordIds;
}

/**
 * 추출된 태그로 TMDB API를 호출하여 영화/드라마 리스트(후보군)를 추림
 */
async function getCandidatesFromTMDB(aiTagsObject, url) {
    console.log("3. TMDB API로 후보군 20개 검색");

    if (!aiTagsObject || !aiTagsObject.genres || aiTagsObject.genres.length === 0) {
        console.error("전달된 장르가 없습니다.");
        return [];
    }

    try {
        const response = await fetch(url);
        const data = await response.json();

        const candidates = buildMovieCandidateList(data.results || []);
        console.log(candidates)
        renderMoviePreview(candidates); // 개발 단계에서 확인용으로 화면에 뿌리기
        return candidates;

    } catch (error) {
        console.error("TMDB 호출 오류:", error);
        return [];
    }
}

/**
 * 영화 이름으로 추천 후보 리스트 가공
 */
function buildMovieCandidateList(results) {
    return results.map(movie => {
        return {
            id: movie.id,
            title: movie.title,
            release_date: movie.release_date,
        };
    });
}

/**
 * 개발 단계에서 확인용으로 화면에 뿌리기
 */
function renderMoviePreview(movieList) {
    let table = [];
    table.push("<hr><table><tr><td>영화명</td><td>이미지</td></tr>");

    for (const movie of movieList) {
        // 포스터 경로가 있으면 <img> 태그를 만들고, 없으면 '이미지 없음' 글자를 띄웁니다.
        let posterImg = movie.poster_path
            ? `<img src="https://image.tmdb.org/t/p/w200${movie.poster_path}" alt="${movie.title} 포스터">`
            : "이미지 없음";
        table.push(`
            <tr>
                <td>${movie.title}</td>    
                <td>${posterImg}</td>
            </tr>
        `);
    }

    table.push("</table>")
    document.getElementById('movie-output').innerHTML += table.join('\n');
}

/**
 * [Step 3] 후보군 리스트와 사용자 정보를 다시 OpenAI에 보내어 최종 3개를 고르고 이유를 작성받음
 */
async function getFinalRecommendations(userInfo, candidates) {
    console.log("3. AI가 최종 후보 3개 선정 및 추천 이유 작성");
    // TODO: OpenAI API 호출 (prompt: 사용자 정보와 이 20개 리스트를 줄게. 여기서 3개만 고르고 이유를 적어줘 JSON으로)
    // Return 예시: [{ id: 101, reason: "주인공의 상황이 당신과 비슷해서 위로가 될 거예요." }]
    return [{ id: 101, reason: "이유입니다." }];
}

/**
 * 전체 흐름을 제어하는 메인 API 함수
 */
async function runRecommendationFlow(userInfo) {
    const tags = await getSearchTagsFromAI(userInfo);
    const candidates = await getCandidatesFromTMDB(tags);
    const finalPicks = await getFinalRecommendations(userInfo, candidates);

    return { candidates, finalPicks }; // app.js로 데이터 전달
}

