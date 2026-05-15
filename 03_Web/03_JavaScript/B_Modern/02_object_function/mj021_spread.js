/*
spread 와 rest
ES6 에서 도입된 spread 와 rest 

spread (전개구문)
  배열 과 같은 iterable 한 객체를
    0개 이상의 인소 또는 요소로 펼칠수있습니다.
      (즉 0개 이상의 key-value 상으로 객체 확장)

https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Spread_syntax

  기존 객체를 '복사'하고, 그리고 뭔가 더 추가하고자 할때 사용

spread 구문]
  함수 호출:
    myFunction(...iterableObj);
  
  배열 리터럴과 문자열:
    [...iterableObj, '4', 'five', 6];

  객체 리터럴(ECMAScript 2018에서 추가)
    let objClone = { ...obj };
*/

{
  const slime = {
    name: "슬라임"
  };

  const cuteSlime = {
    name: "슬라임",
    style: "cute" // property 추가
  };

  const purpleCuteSlime = {
    name: "슬라임",
    style: "cute",
    color: "purple" // property 또 추가..
  };

  console.log(slime);
  console.log(cuteSlime);
  console.log(purpleCuteSlime);
}

// 기존의 객체에서 만들어진 속성을 사용하여
// '새로운' 객체를 만들때 spread 를 사용하면 편리
// ...  : spread 연산자
console.log();

{
  const slime = {
    name: "슬라임"
  };
  const cuteSlime = {
    ...slime,  // 기존 slime 의 key-value (들)이 전개(spread) 된다.
    style: "cute",   // 추가할 key-value
  };
  const purpleCuteSlime = {
    ...cuteSlime,
    color: 'purple',
  };

  console.log(slime);
  console.log(cuteSlime);
  console.log(purpleCuteSlime);

  // ⭐️ spread 연산자로 생성된 객체는 복제된 '새로운' 객체다.
  const smallSlime = {...slime};
  const megaSlime = slime;

  console.log();
  console.log('slime', slime);
  console.log('smallSlime', smallSlime);
  console.log('megaSlime', megaSlime);

  console.log(slime == megaSlime);  // true: 동일객체
  console.log(slime == smallSlime); // false: 다른객체

  // 기존 property 값을 변경한 '새로운' 객체 생성
  let greenCuteSlime = {
    ...purpleCuteSlime,
    color: "Green",  // color 값 덮어쓰기
  };
  console.log('🌐', greenCuteSlime);

  // spread 순서 주의
  greenCuteSlime = {
    color: "Green",
    ...purpleCuteSlime,
  };
  console.log('🌐', greenCuteSlime);


}


// 만약 spread 를 사용하지 않으면 어떨까?
console.log();
{
  const slime = {
    name: "슬라임"
  };

  const cuteSlime = slime;  // cuteSlime 은 slime 과 동일 객체 참조
  cuteSlime.style = 'cute';

  console.log(slime);
  console.log(cuteSlime);
  console.log(cuteSlime == slime);
}


console.log()
// spread 연산자는 배열에서도 사용 할 수 있습니다.
{
  const animals = ["개", "고양이", "참새"];
  let pets = [...animals, "비둘기"];

  console.log(animals);
  console.log(pets);

  pets = ["닭둘기", ...animals];
  console.log(pets);



}

// 배열에서 spread 연산자를 여러번 사용 할 수도 있습니다.
{
  
  const numbers = [1, 2, 3, 4, 5];
  console.log([...numbers, 1000, ...numbers]);
  // console.log([...numbers, ...numbers]);

}

//────────────────────────────────────────────────────────────────────

