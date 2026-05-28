/**
 * OpenAI API 호출 및 응답 처리
 */
async function callOpenAi(promptInput) {

    const requestBody = {
        model: CONFIG.OPENAI_MODEL_NAME,
        messages: [
            {
                role: "user",
                content: promptInput
            }
        ],
        temperature: 0.7
    };

    const response = await fetch(CONFIG.OPENAI_API_ENDPOINT, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${CONFIG.OPENAI_KEY}`
        },
        body: JSON.stringify(requestBody)
    });

    // HTTP 상태 코드 확인
    if (!response.ok) {
        const detail = await response.text().catch(() => "");
        throw new Error(`OpenAI API 요청 실패 (HTTP ${response.status})`);
    }
    const data = await response.json();

    // OpenAI 응답 텍스트 추출
    return data.choices?.[0]?.message?.content ?? null;
}