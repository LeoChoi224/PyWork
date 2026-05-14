/******************************
 * 배열의 reduce : n개의 입력 => 1개의 출력 
 * reduce 함수는 잘 사용 할 줄 알면 정말 유용한 내장 함수입니다. 
 * 
 * reduce(callback함수)
 * reduce(callback함수, 초깃값)
 * 
 * reduce 함수를 누적계산결과'값'을 리턴한다
 * (previous, current) => 누적계산결과
 * (previous, current, index, array) => 누적계산결과
 *   - index: 현재 current 가 몇번째 인지 
 *   - array: 함수를 실행하는 배열 자신 
 * 
 * ES5 등장
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
 */

// 아래 주어진 배열에 대하여 '총합'을 구하기
let numbers = [1, 2, 3, 4, 5]
let result, sum

sum = numbers.reduce((prev, cur) => prev + cur)
console.log('sum =', sum);
// [1, 2, 3, 4, 5]
//   ↘↓
// [   3, 3, 4, 5]
//      ↘↓
// [      6, 4, 5]
//         ↘↓
// [        10, 5]
//            ↘↓
// [           15]

sum = numbers.reduce((prev, cur) => prev + cur, 0)
console.log('sum =', sum);
// [0, 1, 2, 3, 4, 5]   초깃값 0 부터 시작
//   ↘↓
// [   1, 2, 3, 4, 5]
//      ↘↓
// [      3, 3, 4, 5]
//         ↘↓
// [         6, 4, 5]
//            ↘↓
// [           10, 5]
//               ↘↓
// [              15]

// 중간 과정 확인
sum = numbers.reduce((prev, cur, index) => {
    let result = prev + cur;
    console.log(`🥎${index}: ${prev} + ${cur}`);
    return result;
}, 0)
console.log('sum =', sum);

// [1, 2, 3, 4, 5]  n개의 데이터로부터 x2배 한
// --> [ 2, 4, 6, 8, 10 ]

//------------------------------------------------
//  원래 reduce : n개 -> 1개
//  그러나 다음의 동작도 가능하다.

// 각각의 원소에 x 2을 한 배열 구하기
// [1, 2, 3, 4, 5]  n개의 데이터로부터
// --> [ 2, 4, 6, 8, 10 ]  라는 1개의 '배열' 데이터 생성
// (응? 이건 map 아닌가?)

// result = numbers.reduce((prev, cur) => {
//     prev.push(cur * 2);
//     return prev;
// }, []);  // <- 초깃값 []
result = numbers.reduce((prev, cur) => 
    prev.push(cur * 2) && prev
, []);  // <- 초깃값 []
console.log(result);

//----------------------------------------------------------
// filter 동작 을 reduce 로 만들어 보기
// [1, 2, 3, 4, 5]  에서 짝수만 걸러내기
//     ↓     ↓
// [   2,    4   ]
console.log();

result = numbers.reduce((prev, cur) => {
    if(cur % 2 == 0) prev.push(cur);
    return prev;        
}, []);
console.log(result);


