/**
 * 사용자 입력 데이터 검증
 */
function getUserInput() {
    let frm = document.forms.infoForm;
    let mbti = frm.mbti?.value?.trim().toUpperCase() || "";

    // MBTI 유효성 검증
    if (mbti && !/^[EI][SN][TF][JP]$/i.test(mbti)) {
        alert(`"${mbti}"는 유효한 값이 아닙니다. 💢\n MBTI를 입력 하세요. 예: ISTP`);
        frm.mbti.focus();
        return null;
    } else {
        // 프롬프트에 맞춤 리팩터링
        const userInfo = {
            mbti: mbti ? mbti : "미 입력",
            gender: frm.gender.value == "male" ? "남자" : "여자",
            age: frm.age.value ? `${frm.age.value}세` : "미 입력",
            mood: frm.mood.value.trim() ? `${frm.mood.value.trim()}` : "미 입력",
        }
        return userInfo;
    }
} // end getUserInput()