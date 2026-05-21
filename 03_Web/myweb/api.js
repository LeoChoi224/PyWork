/**
 * OpenAI 및 TMDB API 호출 핵심 로직
 */
const TMDB_url = "https://api.themoviedb.org/3/";
const OPENAI_MODEL_NAME = "gpt-4o";
const OPENAI_API_ENDPOINT = "https://api.openai.com/v1/chat/completions";
const GEMINI_MODEL_NAME = "gemini-2.5-flash";
const GEMINI_API_ENDPOINT = `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL_NAME}:streamGenerateContent?key=${CONFIG.GEMINI_KEY}`;

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
 * AI에게 사용자 정보를 보내 분석을 받고, 실시간 화면 표시 후 태그 객체 리턴
*/
// Gemini 버전
async function getSearchTagsFromAI() {
    console.log("1. 사용자 정보 분석 및 태그 추출 시작");
    const inputData = getUserInput();
    if (!inputData) return null; // 유효성 검사 실패 시 중단

    const outputElement = document.getElementById('output');

    const promptInput = `
너는 사용자의 개인 정보와 현재 심리 상태를 분석하여(입력된 정보로만 분석), TMDB(The Movie Database) API 검색에 가장 적합한 검색용 '장르'와 '소재 키워드'를 한글로 추출하는 데이터 분석가야.

[사용자 정보]
- MBTI: ${inputData.mbti}
- 성별 및 나이: ${inputData.gender}, ${inputData.age}
- 현재 기분/요청사항: "${inputData.mood}"

[임무]
위 정보를 바탕으로 사용자의 취향과 현재 기분에 완벽히 부합하는 영화를 TMDB에서 검색할 수 있도록 아래 [출력 형식]을 엄격히 준수하여 사용자기 읽기좋은 한글 텍스트로 답변해줘. 다른 설명이나 마크다운 기호(\`\`\`json)는 절대 붙이지 마.

[출력 형식]
### 📊 사용자 맞춤 심리 분석
(여기에 사용자의 MBTI와  와 연령대(나이 x, 예: 30대 초반), 성별, 현재 기분 상태를 요약한 다정한 분석 글을 3줄 이내로 작성해줘)

---

### 🎬 검색 매칭 태그
**추천 장르**: (여기에 TMDB 기준 추천 장르 명칭 2개를 쉼표로 구분해서 작성해. 예: 드라마, 액션)\n
**추천 키워드**: (여기에 검색 효율이 좋은 구체적인 영화 소재 한글 키워드 4개를 쉼표로 구분해서 작성해. 예: 시한부, 슬픈 이별, 가족애, 눈물샘)
`;

    console.log(promptInput);
    outputElement.innerHTML = "<i class='fas fa-spinner fa-spin'></i>응답 생성 중... 잠시 기다려주십시오."
    outputElement.classList.add('loading');

    // request body (요청 본문)
    const requestBody = {
        contents: [{
            parts: [{ text: promptInput }]
        }],
    };

    try {
        // 1. Fetch API를 사용하여 요청을 보냅니다.
        const response = await fetch(GEMINI_API_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        outputElement.classList.remove('loading');

        // 2. HTTP 상태 코드 확인
        if (!response.ok) {
            outputElement.innerHTML = `<span style="color: red;">API 요청 실패 (HTTP ${response.status})</span>`;
            return null;
        }

        // 응답 본문을 ReadableStream으로 가져옵니다.
        const reader = response.body
            .pipeThrough(new TextDecoderStream())
            .getReader()

        outputElement.textContent = "";

        // 스트림을 비동기적으로 읽습니다. TODO 스트림 속도 낮추고 비동기로 진행하며 다른 작업 끝내기
        let textContent = "";

        while (true) {
            // value: 생성된 토큰,  done: 생성종료 여부
            const { value, done } = await reader.read();
            if (done) break;  // 스트림 종료

            // 들어온 텍스트 조각을 모아둡니다.
            textContent += value;

            // 제미나이 스트리밍 응답 덩어리에서 "text": "..." 부분만 정규식으로 안전하게 뽑아내는 팁입니다.
            // JSON 전체를 통째로 파싱하려 하면 대괄호나 쉼표 때문에 무조건 깨집니다.
            const regex = /"text"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"/g;
            let match;
            let displayHTML = "";

            // 텍스트 조각만 추출해서 화면에 누적 렌더링
            while ((match = regex.exec(textContent)) !== null) {
                // 유니코드 변환 및 줄바꿈 처리 처리 후 마크다운 파싱
                let cleanText = match[1].replace(/\\n/g, '\n').replace(/\\"/g, '"');
                displayHTML += cleanText;
            }

            outputElement.innerHTML = marked.parse(displayHTML);
            outputElement.scrollIntoView({ block: 'end', behavior: 'smooth' });
        } // end while

        // 스트리밍 완료 후: 문자열 추출 및 오브젝트 화
        // 최종적으로 완성된 화면 글자(HTML 아님, 텍스트 원본)를 가져옵니다.
        const finalRawText = outputElement.innerText;
        console.log("AI 최종 답변 텍스트:\n", finalRawText);

        // 정규식이나 간단한 문자열 자르기로 장르와 키워드 라인을 쏙 빼옵니다.
        try {
            const genreLine = finalRawText.split("추천 장르")[1]?.split("\n")[0] || "";
            const keywordLine = finalRawText.split("추천 키워드")[1]?.split("\n")[0] || "";

            // 기호(:, 괄호)들을 정리하고 쉼표 기준 배열로 만듭니다.
            const cleanGenres = genreLine.replace(/[:\s()]/g, "").split(",");
            const cleanKeywords = keywordLine.replace(/[:\s()]/g, "").split(",");

            // 다음 스텝으로 가기 편하게 "순수 자바스크립트 객체"로 조립합니다.
            const aiTagsObject = {
                genres: cleanGenres,       // 예: ["드라마", "로맨스"]
                keywords: cleanKeywords    // 예: ["시한부", "슬픈이별", "가족애", "눈물샘"]
            };

            console.log("성공적으로 생성된 자바스크립트 오브젝트:", aiTagsObject);
            getKeywordIdFromTMDB(aiTagsObject);
            getCandidatesFromTMDB(aiTagsObject);
            // return aiTagsObject; // 이 오브젝트가 Step 2 함수의 매개변수(tags)로 전달됩니다!

        } catch (parseError) {
            console.error("텍스트에서 태그를 오브젝트로 가공하는데 실패했습니다:", parseError);
            return null;
        }

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
 * keyword Id 가져오기
*/
async function getKeywordIdFromTMDB(tags) {
    if (!tags || !tags.keywords || tags.keywords.length === 0) {
        console.error("전달된 키워드가 없습니다.");
        return [];
    }
    console.log("2. TMDB API로 키워드 ID 검색");

    const keywords = [];
    for (let i = 0; i < tags.keywords.length; i++) {
        let tmdbSearchKeywordUrl =`
        ${TMDB_url}search/keyword?
        query=${tags.keywords[i]}
        &api_key=${CONFIG.TMDB_KEY}`;

        try {
            const response = await fetch(tmdbSearchKeywordUrl);
            const data = await response.json();

            const keywordId = data?.results?.[0]?.id;
            keywordId && keywords.push(keywordId);

        } catch (error) {
        console.error("TMDB 호출 오류:", error);
        return []; 
        }
    }
    return keywords;
}

/**
 * [Step 2] 추출된 태그로 TMDB API를 호출하여 영화/드라마 리스트(후보군)를 추림
 */
async function getCandidatesFromTMDB(tags) {
    if (!tags || !tags.genres || tags.genres.length === 0) {
        console.error("전달된 장르가 없습니다.");
        return [];
    }
    console.log("3. TMDB API로 후보군 20개 검색");

    const first_genres_id = GENRES[tags.genres[0]];
    const second_genres_id = GENRES[tags.genres[1]];
    console.log(`TMDB 검색에 사용할 장르: [${tags.genres[0]}=${first_genres_id}, ${tags.genres[1]}=${second_genres_id}]`);
    
    

    const tmdbSearchUrl =`
    ${TMDB_url}discover/movie?
    include_adult=false
    &language=ko-KR
    &page=1
    &with_genres=${first_genres_id}|${second_genres_id}
    &with_keywords=${keywords[0]}|${keywords[1]}
    &sort_by=popularity.desc
    &api_key=${CONFIG.TMDB_KEY}`;
			
    try {
        const response = await fetch(tmdbSearchUrl);
        const data = await response.json();
        const candidates = data.results || [];
        parseJSON(data);
        console.log(candidates)
        // console.log(`TMDB에서 '${searchKeyword}' 후보 영화 ${candidates.length}개 찾음 완료.`);
        // return candidates;

    } catch (error) {
        console.error("TMDB 호출 오류:", error);
        return [];
    }
    // outputElement.innerHTML = marked.parse(displayHTML);
    // outputElement.scrollIntoView({ block: 'end', behavior: 'smooth' });
    // return [{ id: 101, title: "테스트 영화", overview: "슬픈 영화입니다." }];
}

function parseJSON(jsonObj) {
    let table = [];
    table.push("<hr><table><tr><td>영화명</td><td>이미지</td></tr>");

    for (e of jsonObj.results) {
        // 포스터 경로가 있으면 <img> 태그를 만들고, 없으면 '이미지 없음' 글자를 띄웁니다.
        let posterImg = e.poster_path
            ? `<img src="https://image.tmdb.org/t/p/w200${e.poster_path}" alt="${e.title} 포스터">`
            : "이미지 없음";
        table.push(`
            <tr>
                <td>${e.title}</td>    
                <td>${posterImg}</td>
            </tr>
        `);
    }

    table.push("</table>")
    document.getElementById('output').innerHTML = document.getElementById('output').innerHTML + table.join('\n');
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




// AI 한테 받은 값들로 tmdb 에서 값을 가져와 화면에 뿌리기
// async function getCandidatesFromTMDB(tags) {
//     if (!tags || !tags.keywords || tags.keywords.length === 0) {
//         console.error("전달된 태그나 키워드가 없습니다.");
//         return [];
//     }
//     console.log("2. TMDB API로 후보군 20개 검색");
//     // TODO: TMDB의 /discover/movie API에 tags.genre_ids를 넣어서 호출
//     // Return 예시: [{ id: 1, title: "영화A", overview: "..." }, ... 20개]
//     // 첫 번째 한글 키워드를 검색어로 지정 (예: "시한부")
//     const first_genres_id = GENRES[tags.keywords[0]];
//     const second_genres_id = GENRES[tags.keywords[1]];
//     console.log(`TMDB 검색에 사용할 핵심 키워드: [${tags.keywords[0]}=${first_genres_id}, ${tags.keywords[1]}=${second_genres_id}]`);

//     const tmdbSearchUrl =
//         `${TMDB_url}discover/movie?
//     include_adult=false
//     &language=ko-KR
//     &page=1
//     &with_genres=${first_genres_id}|${second_genres_id}
//     &sort_by=popularity.desc
//     &api_key=${CONFIG.TMDB_KEY}`;
//     // &with_keywords=1|2
			
//     try {
//         const response = await fetch(tmdbSearchUrl);
//         const data = await response.json();
//         const candidates = data.results || [];
//         parseJSON(data);
//         console.log(candidates)
//         // console.log(`TMDB에서 '${searchKeyword}' 후보 영화 ${candidates.length}개 찾음 완료.`);
//         // return candidates;

//     } catch (error) {
//         console.error("TMDB 호출 오류:", error);
//         return [];
//     }
//     // outputElement.innerHTML = marked.parse(displayHTML);
//     // outputElement.scrollIntoView({ block: 'end', behavior: 'smooth' });
//     // return [{ id: 101, title: "테스트 영화", overview: "슬픈 영화입니다." }];
// }
/**
* Fetch API를 사용하여 Gemini API에 스트리밍 요청을 보내고 응답을 처리합니다.
**/
// async function requestAiRecommendation() {
//     let frm = document.forms.infoForm;

//     // 프롬프트에 맞춤 리팩터링
//     let mbti = frm.mbti.value ? `mbti: ${frm.mbti.value.trim()},` : "";
//     let gender = frm.gender.value.trim() == "male" ? "성별: 남자," : "성별: 여자,";
//     let age = frm.age.value.trim() ? `나이: ${frm.age.value.trim()}` : "";
//     let mood = frm.mood.value.trim() ? `추가 요청사항은 "${frm.mood.value.trim()}" 이고,` : "";

//     const outputElement = document.getElementById('output');
//     const promptInput =
//         `내가 좋아할만한 영화를 추천 받고싶어.
//         내 정보는 ${mbti} ${gender} ${age}이야. ${mood} 이 정보로 영화 추천해줘`;

//     console.log(promptInput);
//     outputElement.innerHTML = "<i class='fas fa-spinner fa-spin'></i>응답 생성 중... 잠시 기다려주십시오."
//     outputElement.classList.add('loading');

//     // request body (요청 본문)
//     // const prompt = promptInput.value.trim();
//     const requestBody = {
//         contents: [{
//             parts: [{ text: promptInput }]
//         }],
//     };

//     try {
//         // 1. Fetch API를 사용하여 요청을 보냅니다.
//         const response = await fetch(GEMINI_API_ENDPOINT, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(requestBody)
//         });

//         outputElement.classList.remove('loading');

//         // 2. HTTP 상태 코드 확인
//         if (!response.ok) {
//             const errorJson = await response.json();
//             const errorMessage = errorJson?.error?.message || `HTTP 오류: ${response.status}`;  // 호출실패하면 응답에 error 키가 있다.
//             outputElement.textContent = `API 요청 실패: ${errorMessage}`;
//             console.error("API Error Response:", errorJson);
//             return;
//         }

//         // 응답 본문을 ReadableStream으로 가져옵니다.
//         const reader = response.body
//             .pipeThrough(new TextDecoderStream())
//             .getReader()

//         outputElement.textContent = "";

//         // 스트림을 비동기적으로 읽습니다.
//         let textContent = "";

//         while (true) {
//             // value: 생성된 토큰,  done: 생성종료 여부
//             const { value, done } = await reader.read();
//             if (done) break;  // 스트림 종료

//             // 들어온 텍스트 조각을 모아둡니다.
//             textContent += value;

//             // 제미나이 스트리밍 응답 덩어리에서 "text": "..." 부분만 정규식으로 안전하게 뽑아내는 팁입니다.
//             // JSON 전체를 통째로 파싱하려 하면 대괄호나 쉼표 때문에 무조건 깨집니다.
//             const regex = /"text"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"/g;
//             let match;
//             let displayHTML = "";

//             // 텍스트 조각만 추출해서 화면에 누적 렌더링
//             while ((match = regex.exec(textContent)) !== null) {
//                 // 유니코드 변환 및 줄바꿈 처리 처리 후 마크다운 파싱
//                 let cleanText = match[1].replace(/\\n/g, '\n').replace(/\\"/g, '"');
//                 displayHTML += cleanText;
//             }

//             outputElement.innerHTML = marked.parse(displayHTML);
//             outputElement.scrollIntoView({ block: 'end', behavior: 'smooth' });

//         } // end while
//     } catch (error) {
//         console.error("Fetch 또는 스트림 처리 중 오류 발생:", error);
//         outputElement.textContent = `오류 발생: ${error.message}`;
//     }
// } // end streamGeminiResponse()

// /**
//  * API 키를 저장할 객체 🚨[미니 프로젝트 전용] 추후 삭제 코드
//  * Live server 사용시 숨김 파일을 읽어오지 못함 참고용으로 코드 는 그대로 남겨둠
//  */
// const CONFIG = {
//     TMDB_KEY: "",
//     OPENAI_KEY: "",
//     GEMINI_KEY: ""
// };

// /**
//  * 환경변수 파일을 읽어오는 함수
//  */
// async function loadEnv() {
//     try {
//         // 상위 폴더에 있는 .env 파일을 fetch로 가져옴
//         const response = await fetch('../.env');
//         const text = await response.text();

//         // 줄바꿈으로 쪼개서 키와 값을 분리
//         text.split('\n').forEach(line => {
//             const [key, value] = line.split('=');
//             if (key && value) {
//                 if (key.trim() === 'TMDB_API_KEY') CONFIG.TMDB_KEY = value.trim();
//                 if (key.trim() === 'OPENAI_API_KEY') CONFIG.OPENAI_KEY = value.trim();
//                 if (key.trim() === 'GEMINI_API_KEY') CONFIG.GEMINI_KEY = value.trim();
//             }
//         });

//         console.log("환경 변수 로드 완료!");
//     } catch (error) {
//         console.error(".env 파일을 읽어오는데 실패했습니다:", error);
//     }
//     // 🚀 앱 시작 시 가장 먼저 실행되도록 설정
//     // 예: 
//     // loadEnv().then(() => { runRecommendationFlow(userInfo); });
// } // end loadEnv()