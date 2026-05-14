/**
   * Nullish coalescing operator (??, ?)   널 병합 연산자.
   * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing
   * 
   * nullish 란?  => null 혹은 undefined
   * 
   *   ES2020 에 소개
   */

result = 10 ?? 20;
console.log(result);

result = null ?? 20;
console.log(result);

result = undefined ?? '하석';
console.log(result);

result = null;
result = result ?? 'default';
// 이렇게도 가능 -> result ??= 'default';
console.log(result);


console.log('\n🟦 Optional chaining');

let member, getCity;

getCity = function(user){
    return user.address.city;
};

member = { address: {city: '서울'}};
console.log(getCity(member));

// member = null;
// member = { address: null};
// console.log(getCity(member));


// 이를 && 연산자 SCE 로 검증하게 되면...
getCity = function(user) {
    city = user && user.address && user.address.city
    return city || "도시명이 없습니다";  // 대체값
}
// getCity = function(user) {
//     return user && user.address && user.address.city
// }

member = null; // 죽지않고 null 리턴
member = { address: null};
console.log(getCity(member))

// 문제점....
// city = user && user.address && user.address.city
//    길고 반복적이다...
//   --> Optional Chaining 등장!

  /**
   * Optional chaining (?.)
   * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining
   *
   *  객체의 속성에 접근할 때, 중간 경로가 null이나 undefined 여도 에러를 던지지 않고
   *  undefined를 반환하도록 해주는 문법이에요.
   *
   *  ES2020(ES11)에 도입
   *
   * [세가지 사용형태]
   *  obj?.prop    속성 접근
   *  obj?.[expr]   대괄호 표기법 (동적 키)
   *  func?.(args)  함수/메서드 호출
   */
 
  // . <- 이걸 chaining 연산자 라고 한다

member = {name: "신하석"};
  //   console.log(member.address.city);  // TypeError: Cannot read properties of undefined (reading 'city')

console.log(member?.address?.city);  // undefined 에러 없음!
// ?. 왼쪽 값이 null 또는 undefined면, 그 시점에서 평가를 멈추고 undefined를 반환합니다. 
// 즉, *단락 평가(short-circuit)* 동작 수행

member = {
    name: "신하석",
    greet: function() {return "Hello";},
}

console.log(member?.name); 
console.log(member?.['name']);
console.log(member.greet?.());
console.log(member.sayBye?.()); // undefined 
// console.log(member?.sayBye());
// console.log(member.sayBye.());
// console.log(member.name?.());

// && 는 0, "", false 같은 falsy 값에서도 멈추지만, 
// ?.는 오직 null과 undefined 에서만 멈춥니다

// 기본값을 주고 싶을때 "??" 와 같이 사용
getCity = function(user) {
    return user?.address?.city ?? "도시명이 없습니다"
}

console.log(getCity(null));  // "도시명이 없습니다"
console.log(getCity({address: undefined}));  // "도시명이 없습니다"


// API 호출 응답. DOM 조회결과 , 콜백호출 같은 곳에서 특히 유용하다.

// 남용금지: nullish 가 확실하게 아닌곳까지 ?. 을 붙이면... 버그 발생시 
//          조용히 undefined 로 숨겨서 디버깅을 어렵게 할수 있다.

