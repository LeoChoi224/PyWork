function add(a, b){
    console.log('a =',a, ', b =', b)
    return a + b
}
let sum = 0

sum = add(1, 2)
console.log('sum =', sum) // 3

sum = add(10, 20, 30)  // 호출시 매개변수가 더 많은 경우
console.log('sum =', sum) // 30

sum = add(10) // 호출시 매개변수가 더 적은 경우. 이경우 b 는 undefined 가 된다.
console.log('sum =', sum) // NaN

//------------------------------------------
//  함수의 기본 파라미터 (default function parameter)
//  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Default_parameters

let circleArea = function (r) {
  return Math.PI * r * r;
};

let area = circleArea(4);
console.log(area); // 50.26548245743669

// 매개변수가 없다면??
area = circleArea();
console.log(area);

// 매개변수 검증 : SCE 사용
circleArea = function(r){
  let radius = r || 1;  // r 이 없으면 기본값 1
  return Math.PI * (radius ** 2);
}
console.log();
console.log(circleArea(4));
console.log(circleArea());

// 함수 기본 파라미터 설정
circleArea = function(r = 1){
  return Math.PI * (r ** 2);
}
console.log();
console.log(circleArea(4));
console.log(circleArea());

// // 화살표함수도 함수 기본 파라미터 사용 가능.
circleArea = (r = 100) => Math.PI * (r ** 2);
console.log();
console.log(circleArea(4));
console.log(circleArea());


