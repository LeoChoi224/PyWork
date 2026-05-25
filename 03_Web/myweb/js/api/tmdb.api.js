/**
 * TMDB API 호출 및 영화 데이터 처리
 */

/**
 * 명작 후보 (최신 조건 x) URL
 */
const buildClassicMovieUrl = (genreIds, keywordIds) => {
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
 * 최신 후보 (최근 2년) URL
 */
const buildRecentMovieUrl = (genreIds, keywordIds) => {
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
 * 키워드 ID URL
 */
const buildKeywordIdUrl = (keyword) => {
    return `${CONFIG.TMDB_URL}search/keyword?query=${encodeURIComponent(keyword)}&api_key=${CONFIG.TMDB_KEY}`;
}
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
        const url = buildKeywordIdUrl(keyword);

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
} // end getKeywordIdFromTMDB()

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
        // renderMoviePreview(candidates); // 개발 단계에서 확인용으로 화면에 뿌리기
        return candidates;

    } catch (error) {
        console.error("TMDB 호출 오류:", error);
        return [];
    }
} // end getCandidatesFromTMDB()


/**
 * TMDB 영화 상세 정보 조회
 */
async function getMovieDetail(movie) {
    console.log("5. 최종 3개 영화의 상세 정보를 요청");

    const url = `
${CONFIG.TMDB_URL}movie/${movie.id}
?api_key=${CONFIG.TMDB_KEY}
&language=ko-KR
&append_to_response=credits,videos,similar
`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`TMDB 요청 실패: ${response.status}`);
        }

        const data = await response.json();
        const results = buildMovieDetail(data, movie);
        console.log("getMovieDetail", results);

        return results;
    } catch (error) {
        console.error("영화 상세 조회 실패:", error);
        return null;
    }
}