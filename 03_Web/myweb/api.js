// OpenAI 및 TMDB API 호출 핵심 로직

/**
 * API 키를 저장할 객체 🚨[미니 프로젝트 전용] 추후 삭제 코드
 */
const CONFIG = {
    TMDB_KEY: "",
    OPENAI_KEY: "",
    GEMINI_KEY: ""
};

/**
 * 환경변수 파일을 읽어오는 함수
 */
async function loadEnv() {
    try {
        // 상위 폴더에 있는 .env 파일을 fetch로 가져옴
        const response = await fetch('../../../.env');
        const text = await response.text();

        // 줄바꿈으로 쪼개서 키와 값을 분리
        text.split('\n').forEach(line => {
            const [key, value] = line.split('=');
            if (key && value) {
                if (key.trim() === 'TMDB_API_KEY') CONFIG.TMDB_KEY = value.trim();
                if (key.trim() === 'OPENAI_API_KEY') CONFIG.OPENAI_KEY = value.trim();
                if (key.trim() === 'GEMINI_API_KEY') CONFIG.GEMINI_KEY = value.trim();
            }
        });

        console.log("환경 변수 로드 완료!");
    } catch (error) {
        console.error(".env 파일을 읽어오는데 실패했습니다:", error);
    }
    // 🚀 앱 시작 시 가장 먼저 실행되도록 설정
    // 예: 
    // loadEnv().then(() => { runRecommendationFlow(userInfo); });
} // end loadEnv()

const TMDB_url = "https://api.themoviedb.org/3/";
// const OPENAI_MODEL_NAME = "gpt-4o";
// const OPENAI_API_ENDPOINT = "https://api.openai.com/v1/chat/completions";
const GEMINI_MODEL_NAME = "gemini-2.5-flash"; // 스트리밍을 지원하는 모델
const GEMINI_API_ENDPOINT = `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL_NAME}:streamGenerateContent?key=${CONFIG.GEMINI_KEY}`;

/**
 * 사용자 정보 받기 & 검증
 */
function getUserInput() {
    let frm = document.forms.infoForm;
    // let search_tags_url = `${OPENAI_API_ENDPOINT}`;

    loadEnv()
    console.log(CONFIG.GEMINI_KEY)
    console.log(frm)
    console.log(frm.gender.value)
    // 유효성 검사

} // end getUserInput()
/**
 * <form id=​"infoForm">
 *      <select id=​"gender">​…​</select>​
 *      <input type=​"number" id=​"age" placeholder=​"나이">​
        <input type=​"text" id=​"mbti" placeholder=​"MBTI (예:​ INFP)​">​
        <textarea id=​"mood" placeholder=​"오늘 기분이 어떠신가요? (예:​ 우울해서 펑펑 울고싶어)​">​</textarea>​
        <button type=​"button" onclick=​"requestAiRecommendation()​">​AI에게 추천받기​</button>​</form>​
 */

/** 
* Fetch API를 사용하여 Gemini API에 스트리밍 요청을 보내고 응답을 처리합니다.
**/
function requestAiRecommendation() {
    let search_tags_url = `${GEMINI_API_ENDPOINT}`;
    let frm = document.forms.infoForm; // 중복제거 TODO
    let gender = frm.gender.value == "male" ? "남자" : "여자"

    const outputElement = document.getElementById('output');
    const promptInput =
    `내가 좋아할만한 영화를 추천 받고싶어. 내 정보는 mbti: ${frm.mbti.value}, 
    성별: ${gender}, 나이: ${frm.age.value}이야.
    ${frm.mood.value || ""}. 이 정보로 영화 추천해줘`; 

    outputElement.innerHTML = "<i class='fas fa-spinner fa-spin'></i>응답 생성 중... 잠시 기다려주십시오."
    outputElement.classList.add('loading');


    try {
        // 1. Fetch API를 사용하여 요청을 보냅니다.
        const response = await fetch(API_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        outputElement.classList.remove('loading');

        // 2. HTTP 상태 코드 확인
        if (!response.ok) {
            const errorJson = await response.json();
            const errorMessage = errorJson.error.message || `HTTP 오류: ${response.status}`;  // 호출실패하면 응답에 error 키가 있다.
            outputElement.textContent = `API 요청 실패: ${errorMessage}`;
            console.error("API Error Response:", errorJson);
            return;
        }

        // 응답 본문을 ReadableStream으로 가져옵니다.
        const reader = response.body
            .pipeThrough(new TextDecoderStream())
            .getReader()

        outputElement.textContent = "";

        // 스트림을 비동기적으로 읽습니다.
        let textContent = "";

        while (true) {
            // value: 생성된 토큰,  done: 생성종료 여부
            const { value, done } = await reader.read();
            if (done) break;  // 스트림 종료

            // 확인
            // outputElement.textContent += '🎃' + value;
            // 각 value 마다 앞에 한글다를 빼면 JSON parser 가 가능한 object 다.

            chunk = value.slice(1).trim();
            if (chunk) {
                try {
                    const data = JSON.parse(chunk);
                    const textChunk = data.candidates?.[0]?.content?.parts?.[0]?.text || '';

                    // outputElement.textContent += '🎃' + value;
                    textContent += textChunk;
                    outputElement.innerHTML = marked.parse(textContent);

                    // 출력 요소의 하단으로 스크롤 되게 하기
                    outputElement.scrollIntoView({ block: 'end', behavior: 'smooth' });

                } catch (e) {
                    console.error("JSON 파싱 오류 또는 데이터 포맷 오류:", e, chunk);
                }

            } // end if

        } // end while



    } catch (error) {
        console.error("Fetch 또는 스트림 처리 중 오류 발생:", error);
        outputElement.textContent = `오류 발생: ${error.message}`;
    }
} // end streamGeminiResponse()




// JSON 요청 url
//     let url = `${req_url}?key=${api_key}
// &movieNm=${movieNm}
// &openStartDt=${openStartDt}
// &itemPerPage=${itemPerPage}
// &curPage=${curPage}`;

/**
 * [Step 1] OpenAI에게 사용자 정보를 보내어 TMDB 검색용 '장르 ID'나 '키워드'를 추천받음
 */
async function getSearchTagsFromAI(userInfo) {
    console.log("1. 사용자 정보 분석 및 태그 추출 시작");
    // TODO: OpenAI API 호출 (prompt: 이 사용자의 기분에 맞는 TMDB 장르 ID를 배열로 줘)
    // Return 예시: { genre_ids: [18, 35], keywords: "sad, healing" }
    return { genre_ids: [18] };
}

/**
 * [Step 2] 추출된 태그로 TMDB API를 호출하여 영화/드라마 리스트(후보군)를 추림
 */
async function getCandidatesFromTMDB(tags) {
    console.log("2. TMDB API로 후보군 20개 검색");
    // TODO: TMDB의 /discover/movie API에 tags.genre_ids를 넣어서 호출
    // Return 예시: [{ id: 1, title: "영화A", overview: "..." }, ... 20개]
    return [{ id: 101, title: "테스트 영화", overview: "슬픈 영화입니다." }];
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