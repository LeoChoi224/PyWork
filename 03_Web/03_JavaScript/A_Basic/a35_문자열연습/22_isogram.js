/*******************************
 * isogram : 중복글자 없는 단어
 * isogram 여부 판단하기 (true/false)
 */

const input = [
    "Dermatoglyphics", // -> true
    "programmer",      // -> false
    "Cocktail",         // -> false  대소문자 동일
    "isogram",         // -> true

    // 다른 입력 데이터로 테스트 필요하면, 배열에 데이터 더 넣어보고 실행해도 됩니다
]


function isIsogram(str) {
    arr = str.toLowerCase().trim().split("")
    return !(str.toLowerCase().trim().split("")
        .some(ch => arr.splice(0, 1) && arr.includes(ch))) // 첫번쨰 값을 뺀 arr에 ch 가 있으면 바로 true 반환
}


input.forEach(e => console.log(isIsogram(e)));