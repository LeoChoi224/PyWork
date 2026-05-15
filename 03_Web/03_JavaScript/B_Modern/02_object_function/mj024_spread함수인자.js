/*
  함수 인자와 spread

  파라미터(parameter) : 함수에서 받아오는 '매개변수'
  인자(argument)  : 함수 호출시 보내는 값
*/
{
  function myFunction(a) {
    // 여기서 a 는 파라미터
    console.log(a);
  }

  myFunction("hello world"); // 여기서 'hello world' 는 인자
}

{
  function sum(...rest) {
    return rest.reduce((a, b) => a + b, 0);
  }
  console.log(sum(1, 2, 3, 4, 5, 6));

  // 그러나...
  const numbers = [1, 2, 3, 4, 5, 6];
  console.log(sum(numbers));  // "01,2,3,4,5,6"

  console.log(sum(
    numbers[0],
    numbers[1],
    numbers[2],
    numbers[3],
    numbers[4],
    numbers[5],
  ));

  // '호출' 시 함수인자에 spread 사용 -> 
  console.log(sum(...numbers));


}

// ⭐️ 파이썬의 args packing, args unpacking 과 비슷.

console.log();

// spread, rest 퀴즈
//------------------------------------------
// 함수에 n 개의 숫자들이 파라미터로 주어졌을 때, 
// 그 중 가장 큰 값을 리턴하세요

/* TODO
function max(????){
  // TODO
}

const data = [1, 2, 3, 4, 10, 5, 6, 7]
const result = max(????)  // data 가 인자로 넘겨져야 한다
console.log(result)   // 결과는 10
*/


//────────────────────────────────────────────────────────────────────