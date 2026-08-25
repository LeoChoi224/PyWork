document.addEventListener("DOMContentLoaded", () => {

    const detectBtn = document.getElementById("detect");
    const textInput = document.getElementById("text");
    const resultElem = document.getElementById("result");

    detectBtn.addEventListener("click", () => {
        const url = "http://127.0.0.1:8000/detect_lang";

        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({text: textInput.value})
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