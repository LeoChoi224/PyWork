/*********************************************
 * every(판별함수)  ES5 등장
 *   배열 안의 '모든' 요소가 주어진 판별 함수를 통과하는지 테스트
 * 
 *   판별함수의 리턴값은 Truthy / Falsy 를 리턴해야 한다
 * 
 *   판별함수의 매개변수 (element, index, array)
 * 
 *   리턴값은 true / false
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/every
 */
console.log('[every]')
let arr1 = [1, 30, 39, 29, 10, 13];

// 배열의 모든 값들이 40 미만인가?
console.log(arr1.every(e => e < 40));  // 6번 호출

// 배열의 모든 값들은 홀수인가?
console.log(arr1.every(e => e % 2 == 1));  // 2번 호출

/**********************************************
 * 배열.some(판별함수)
 *  배열 안의 '어떤' 요소라도 주어진 판별 함수를 통과하는지 테스트
 * 
 *  판별함수의 리턴값은 Truthy / Falsy 를 리턴해야 한다
 * 
 *  판별함수의 매개변수 (element, index, array)
 * 
 *  리턴값은 true / false
 * 
 * ES5 소개
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/some
 */
console.log('-'.repeat(20));
console.log('[some()]');
arr1 = [1, 2, 3, 4, 5];

// 배열값중에 짝수가 있습니까?
console.log(arr1.some(e => e % 2 == 0)) // true, 두번 호출

// 배열값중에 10 보다 큰 값이 있습니까?
console.log(arr1.some(e => e > 10)) // false


