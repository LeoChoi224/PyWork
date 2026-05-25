/**
 * 영화 이미지 URL 생성 유틸 함수
 */

function buildPosterUrl(path, size = "w200") {
    if (!path) return "";
    return `
https://image.tmdb.org/t/p/${size}${path}
`;
}