document.addEventListener("DOMContentLoaded", () => {

    const predictBtn = document.getElementById("btn_iris");
    const resultElem = document.getElementById("result");

     const inputIds = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ];

    predictBtn.addEventListener("click", () => {

        const values = {};

        for (const id of inputIds) {
            const element = document.getElementById(id);
            const input = element?.value?.trim();
            
            if (!input) {
                alert(`${id}를 입력해주세요.`);
                element.focus();
                return null;
            };
            
            if (input < 0) {
                alert(`${id}는 0보다 작을 수 없습니다.`);
                element.focus();
                return null;
            }

            values[id] = input;
        }

        const url = "http://127.0.0.1:8000/predict_iris";

        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(values)
        })
        .then(response => response.json())
        .then(obj => {
            resultElem.textContent = obj.result;
        })
        .catch(error => {
            console.error("Error:", error);
        })
        ;
    });
});

/**
CSR (Client-Side Rendering)방식
  장점: 서버측 부하 줄임.
  단점: 클라이언트 측에 응답한 화면의 내용이 실질적으로 없다.
       -> 검색엔진 최적화 (SEO: Search Engine Optimization) 불리 
       -> 보완: Next.js

SSR (Server-Side Rendering)방식 차이?
  단점: 서버측 과부하 (화면생성연산)

https://youtu.be/iZ9csAfU5Os
 */