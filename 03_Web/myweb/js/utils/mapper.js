/**
 * API 응답 데이터 매핑 처리
 */

/**
 * 프롬프트에 맞춤 리팩터링
 */
function buildUserInfo() {
    return {
    mbti: mbti ? mbti : "미 입력",
    gender: frm.gender.value == "male" ? "남자" : "여자",
    age: frm.age.value ? `${frm.age.value}세` : "미 입력",
    mood: frm.mood.value.trim() ? `${frm.mood.value.trim()}` : "미 입력",
    };
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
} // end buildMovieCandidateList()

/**
 * 영화 상세정보 데이터 가공
 */
function buildMovieDetail(data, movie) {
    return {
        id: data.id,
        title: movie.title,
        original_title: data.original_title,
        poster_path: data.poster_path,
        backdrop_path: data.backdrop_path,
        overview: data.overview,
        tagline: data.tagline,
        release_date: data.release_date,
        runtime: data.runtime,
        vote_count: data.vote_count,
        genres: data.genres,
        production_countries:
            data.production_countries,
        spoken_languages:
            data.spoken_languages,
        director:
            data.credits?.crew?.find(
                person => person.job === "Director"
            ),
        cast:
            data.credits?.cast?.slice(0, 10),
        videos:
            data.videos?.results,
        similar:
            data.similar?.results?.slice(0, 4)
    };
}