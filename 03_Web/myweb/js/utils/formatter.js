/**
 * 문자열 및 데이터 포맷 유틸 함수
 */

function formatAnalysisText(aiTagsObject) {
    const keywords = aiTagsObject.keywords.map((k) => k.ko).join(", ");
    return [
        "📊 사용자 분석",
        aiTagsObject.analysis,
        "",
        "🎬 추천 장르",
        aiTagsObject.genres.join(", "),
        "",
        "🏷 추천 키워드",
        keywords,
    ].join("\n");
}