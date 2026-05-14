/*******************************
 * 영어문장에서 각 단어 첫글자만 대문자 만들기
 */

const input = [
    "i am a PROGRAMMER",     // -> I Am A Programmer
    "THAT ELEPHANT IS BIG",  // -> That Elephant Is Big

    // 다른 입력 데이터로 테스트 필요하면, 배열에 데이터 더 넣어보고 실행해도 됩니다
]

function letterCapitalize(str){
    return str.toLowerCase().trim().split(/\s+/) // 모ems 문자열 소문자로 변환 후 공백 기준 스플릿
        .map(word => word.replace(word[0], word[0].toUpperCase())) // map()으로 첫번쨰 인덱스를 대문자로 변환 후 치환
        .reduce((prev, cur) => prev.concat(" ", cur)) // 공백 기준 join
}

input.forEach(e => console.log(letterCapitalize(e)));