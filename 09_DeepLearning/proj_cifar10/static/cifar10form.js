document.addEventListener("DOMContentLoaded", () => {

    const imageInput = document.getElementById("imageInput");
    const imageContainer = document.getElementById("imageContainer");

    imageInput.addEventListener("change", () => {

        const files = imageInput.files;

        if (files.length === 0) {
            alert("이미지를 선택해주세요!");
            return;
        }

        const formData = new FormData();
        for (const file of files) {
            formData.append("imagefiles", file);
        }

        fetch("/upload", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(obj => {
            imageContainer.innerHTML = "";

            for (const upload of obj.results) {
                imageContainer.innerHTML += `
                <div class="mb-3">
                    <p>업로드된 이미지: <span class="badge bg-success">${upload.label}</span></p>
                    <img src="${upload.url}" alt="미리보기" style="max-width: 300px;">
                </div>
                `;
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});