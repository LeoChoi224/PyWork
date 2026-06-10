// object 를 초기화 하는 구문 (객체 초기자 : object initializer)
//  { property : value, propery : value ... }
let obj, a, b, c;

obj = { a: "foo", b: 42, c: {} };
console.log("obj =", obj);

(a = "foo"), (b = 42), (c = {});
obj = { a: a, b: b, c: c };
console.log("obj =", obj);

// object 를 아래와 같이 정의해도 된다!
// ES6 의 object-shorthand 문법 (단축 속성명)이라고 부릅니다. (이름은 굳이 알아둘 필요는 없습니다..!)
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Object_initializer
(a = "foo"), (b = 42), (c = {});


obj = {a, b, c}; // 속성명(property) 만 나열해도 된다!.  동일 이름의 변수값이 정의되어 있다면!
console.log("obj =", obj);

// obj = {a, b, c, d};  // 정의 되어 있지 않은 이름 -> 에러
                   // ReferenceError: d is not defined

obj = {a, b, c, d: "군포돌이"};  // 가능!
console.log('obj =', obj);



