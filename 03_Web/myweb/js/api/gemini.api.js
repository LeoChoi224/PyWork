/**
 * Gemini AI API 호출 및 응답 처리
 */
async function callGemini(promptInput) {

    const requestBody = {
        contents: [{
            parts: [{ text: promptInput }]
        }],
        generationConfig: {
            responseMimeType: "application/json",
            temperature: 0.7 // 숫자가 작을수록 기계적, 클수록 창의적, 1 이상은 너무 랜덤
        }
    };

    const response = await fetch(CONFIG.GEMINI_API_ENDPOINT, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
    });
    
    // HTTP 상태 코드 확인
      // HTTP 상태 코드 확인
    if (!response.ok) {
        const detail = await response.text().catch(() => "");
        throw new Error(`Gemini API 요청 실패 (HTTP ${response.status})`);
    }
    
    return await response.json();
}