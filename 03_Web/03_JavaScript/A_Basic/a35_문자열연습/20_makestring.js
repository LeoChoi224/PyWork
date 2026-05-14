/*******************************
 * 단어의 앞글자로만 만들어진 문자열 생성
 */

const input = [
    "The community at Code States might be the biggest asset", // -> TcaCSmbtba
    "i am a PROGRAMMER",     // -> iaaP
    "THAT ELEPHANT IS BIG",  // -> TEIB

    // 다른 입력 데이터로 테스트 필요하면, 배열에 데이터 더 넣어보고 실행해도 됩니다
]

function makeString(str){
    
    return str.trim().split(/\s+/) //  공백 기준 스플릿
        .map(word => word[0]) // 첫번째 글자만 배열로
        .reduce((prev, cur) => prev.concat("", cur))
}

input.forEach(e => console.log(makeString(e)));