/**
 * 설정 파일 예시
 */
const CONFIG = {
    /**
     * Secret Key
     */
    TMDB_KEY: "YOUR_KEY",
    OPENAI_KEY: "YOUR_KEY",
    GEMINI_KEY: "YOUR_KEY",

    /**
     * Url, Model
     */
    TMDB_url: "https://api.themoviedb.org/3/",
    OPENAI_MODEL_NAME: "gpt-4o",
    OPENAI_API_ENDPOINT: "https://api.openai.com/v1/chat/completions",
    GEMINI_MODEL_NAME: "gemini-2.5-flash",
};

CONFIG.GEMINI_API_ENDPOINT =
`https://generativelanguage.googleapis.com/v1beta/models/${CONFIG.GEMINI_MODEL_NAME}:streamGenerateContent?key=${CONFIG.GEMINI_KEY}`;

/**
 * 인기 영화 기준 최신 조건 x
 */
const TMDB_CLASSIC_URL = (genreIds, keywordIds) => {
    return `
    ${CONFIG.TMDB_URL}discover/movie?
    include_adult=false
    &language=ko-KR
    &page=1
    &with_genres=${genreIds.join('|')}
    &with_keywords=${keywordIds.join('|')}
    &sort_by=vote_count.desc
    &vote_count.gte=1000
    &api_key=${CONFIG.TMDB_KEY}
    `;
}

/**
 * 최신 영화 기준 최근 2년
 */
const TMDB_RECENT_URL = (genreIds, keywordIds) => {
    return `
    ${CONFIG.TMDB_URL}discover/movie?
    include_adult=false
    &language=ko-KR
    &page=1
    &with_genres=${genreIds.join('|')}
    &with_keywords=${keywordIds.join('|')}
    &primary_release_date.gte=2024-01-01
    &sort_by=popularity.desc
    &vote_count.gte=300
    &api_key=${CONFIG.TMDB_KEY}
    `;
}

/**
 * 장르
 */
const GENRES = {
    "액션": 28,
    "모험": 12,
    "애니메이션": 16,
    "코미디": 35,
    "범죄": 80,
    "다큐멘터리": 99,
    "드라마": 18,
    "가족": 10751,
    "판타지": 14,
    "역사": 36,
    "공포": 27,
    "음악": 10402,
    "미스터리": 9648,
    "로맨스": 10749,
    "SF": 878,
    "TV 영화": 10770,
    "스릴러": 53,
    "전쟁": 10752,
    "서부": 37
};