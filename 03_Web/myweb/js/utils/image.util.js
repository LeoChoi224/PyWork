/**
 * 영화 이미지 URL 생성 유틸 함수
 */

function buildPosterUrl(path, size = "w200") {
    if (!path) return "";
    return `https://image.tmdb.org/t/p/${size}${path}`;
}

/**
 * 메인 화면 영화 포스터 기본 값
 */
const defaultMovies = [
    {
        id: 68721,
        title: "아이언맨 3",
        poster_path: "/5aHoACZhLJR95uQN4Hd2k6swUZq.jpg"
    },
    {
        id: 671,
        title: "해리 포터와 마법사의 돌",
        poster_path: "/8YaP48tVfngbURGldWk1I5odsBK.jpg"
    },
    {
        id: 1726,
        title: "어벤져스",
        poster_path: "/krgjV3rJtBcEpQehODKXNCt6uFL.jpg"
    },
    {
        id: 24428,
        title: "아이언맨",
        poster_path: "/ziReGUV3xURsWmcmsn2GOunPc0L.jpg"
    },
    {
        id: 338953,
        title: "신비한 동물들과 덤블도어의 비밀",
        poster_path: "/uvQbXjMgC5weQepx4jLJJ60H3N0.jpg"
    },
    {
        id: 11178,
        title: "엽기적인 그녀",
        poster_path: "/h7xTfZbrJ86nzypPvPjwVmxZoHS.jpg"
    },
    {
        id: 157336,
        title: "인터스텔라",
        poster_path: "/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
    },
    {
        id: 123025,
        title: "다크 나이트",
        poster_path: "/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
    },
    {
        id: 331251,
        title: "스물",
        poster_path: "/hzKynyDi7NwG5Yxn3JC9eNWM9Io.jpg"
    },
    {
        id: 207703,
        title: "킹스맨: 시크릿 에이전트",
        poster_path: "/pVwvZAgnsuMcDGbeWVtXOpks1oQ.jpg",
    },
    {
        id: 675,
        title: "해리 포터와 불사조 기사단",
        poster_path: "/1ItejykqHTbFWbZXdzqlvqriv7K.jpg"
    },
    {
        id: 10138,
        title: "아이언맨 2",
        poster_path: "/ebJbC9OYAZJxy7bRUGryR72hfa2.jpg"
    },
    {
        id: 634649,
        title: "스파이더맨: 노 웨이 홈",
        poster_path: "/fvqoI9r1GU2EFkc0xjZ6dKCuDVR.jpg"
    },
    {
        id: 129,
        title: "센과 치히로의 행방불명",
        poster_path: "/u1L4qxIu5sC2P082uMHYt7Ifvnj.jpg"
    },
    {
        id: 120,
        title: "반지의 제왕: 반지 원정대",
        poster_path: "/r18JdjImbWDRwkbVDIzWoLQqkCo.jpg"
    },
    {
        id: 496243,
        title: "기생충",
        poster_path: "/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg"
    },
    {
        id: 27205,
        title: "인셉션",
        poster_path: "/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg"
    },
];