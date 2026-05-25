/**
 * API 키 및 환경 설정 관리 예시
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
    TMDB_URL: "https://api.themoviedb.org/3/",
    OPENAI_MODEL_NAME: "gpt-4o",
    OPENAI_API_ENDPOINT: "https://api.openai.com/v1/chat/completions",
    GEMINI_MODEL_NAME: "gemini-2.5-flash",
};

CONFIG.GEMINI_API_ENDPOINT =
`https://generativelanguage.googleapis.com/v1beta/models/${CONFIG.GEMINI_MODEL_NAME}:generateContent?key=${CONFIG.GEMINI_KEY}`;
