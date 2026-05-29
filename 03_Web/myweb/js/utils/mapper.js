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

    // 감독
    const director = data.credits?.crew
        ?.find(person => person.job === "Director");

    // 배우 5명
    const cast = data.credits?.cast
        ?.slice(0, 5)
        ?.map(actor => actor.name);

    // 유튜브 트레일러
    const trailer = data.videos?.results
        ?.find(video =>
            video.site === "YouTube"
            && video.type === "Trailer"
        );

    return {
        id: data.id,
        title: data.title,
        poster_path: data.poster_path,
        overview: data.overview,
        vote_average: data.vote_average,
        runtime: data.runtime,
        release_date: data.release_date,
        genres: data.genres,
        backdrop_path: data.backdrop_path,
        director: director?.name || "정보 없음",
        cast: cast || [],
        trailerKey: trailer?.key || null,
        similar: data.similar?.results?.slice(0, 5) || [],
    };
}