/*
rest
  객체, 배열등의 정해지지 않은 수의 '나머지' 인자들을 받아옴
  비구조화할당(destructuring argument) 나 함수 파라미터에 사용 가능
  
  rest는 생김새는 spread 랑 비슷한데, 역할이 매우 다릅니다.

    https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/rest_parameters


*/

// 객체에서의 rest

{
  const purpleCuteSlime = {
    name: "슬라임",
    attribute: "cute",
    color: "purple"
  };

  const { color, ...rest } = purpleCuteSlime;
  console.log(color);
  console.log(rest);  // color 를 제외한 나머지 것들

  const { attribute, ...준준 } = rest;
  console.log(attribute);
  console.log(준준);

  console.log(purpleCuteSlime);
  // const [ c, ...r ] = purpleCuteSlime;
  // console.log(c);
  // console.log(r);

}


// spread 가 다른 객체, 배열에 퍼뜨리는 역할(?)을 한다면,
// rest 는 나머지들(?) 모아오는 역할.
console.log()

// 배열에서의 rest
{
  const numbers = [0, 1, 2, 3, 4, 5, 6];

  let [zero, ...rest] = numbers;

  console.log(zero);
  console.log(rest); //[ 1, 2, 3, 4, 5, 6 ] 배열

  // rest 는 반드시 마지막에 와야 한다.
  // [...rest, zero] = numbers;  // SyntaxError: Rest element must be last element


}



