/**
 * 사용자 입력 데이터 검증
 */
function getUserInput() {
    const frm = document.getElementById("user-form");
    if (!frm) {
        console.error("user-form 요소를 찾을 수 없습니다.");
        return null;
    }

    const mbti = frm.mbti?.value?.trim().toUpperCase() || "";
    let gender = frm.gender.value
    if (gender) {
        gender = gender == "male" ? "남자" : "여자";
    } else {
        gender = "미 입력"
    }

    // MBTI 유효성 검증
    if (mbti && !/^[EI][SN][TF][JP]$/i.test(mbti)) {
        alert(`"${mbti}"는 유효한 값이 아닙니다. 💢\n MBTI를 입력 하세요. 예: ISTP`);
        frm.mbti.focus();
        return null;
    }
    
        return {
    mbti: mbti ? mbti : "미 입력",
    gender: gender,
    age: frm.age.value ? `${frm.age.value}세` : "미 입력",
    mood: frm.mood.value.trim() ? `${frm.mood.value.trim()}` : "미 입력",
    };
} // end getUserInput()