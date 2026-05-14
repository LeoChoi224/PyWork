/*
    number 타입
    JavaScript 의 숫자타입은 number 타입 '오직 한가지'뿐이다
    number 는 소숫점이 있을수도(실수) / 없을수도(정수) 있다
    number 는 항상 64bit floating point 데이터로 저장된다.
    number의 정밀도(precision)
        - 정수는 15자리까지 정확도 유지
        - 소수점 이하 17자리 정확도 유지
        - 실수간의 연산은 언제나 100% 정확하지 않다 (정밀도 문제)
    number가 가질 수 있는 가장 큰 값은 1.8E308
    
    일반적으로 리터럴(literal) 로 number 생성
        ex) 176, 0b101, 013, 0x0A ...


    NaN (Not a Number) : Number 연산이 안되는 경우 NaN 이 결과값으로 나온다.
    Infinity : 무한대 값

    https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number
*/

let num1, num2, num3;

console.log(123 === 123.0);
console.log(0.2 + 0.1 === 0.3);
console.log(0.2 + 0.1);

console.log('[NaN]');
num1 = 100 / "Apple";
console.log(num1, typeof (num1));
// isNaN()
console.log(isNaN(num1))  // NaN 판정 함수.

// NaN 과의 산술연산 결과는 NaN 이다!
num2 = NaN;
console.log(num2);
console.log(num2 + 5);



/********************************** 
 * 진법 리터럴
 *  0x 로 시작 16진법(hexadecimal)
 *  0 으로 시작 8진법 (octal)
 *  0b 로 시작 2진법 (binary)
 */
console.log('-'.repeat(20))
console.log('[진법리터럴, toString]');

num1 = 24;
let str = num1.toString();
console.log(str, typeof (str));

// 24.toString();  // 숫자 리터럴에 직접 메소드 사용 불가.
(24).toString();  // "24"




/*******************
 * 일반적으로 Number 는 숫자 literal 을 통해 생성되나,
 * object 로서 Number 를 생성할수 있다  (new 사용)  <-- 매우 비추함!  예측하지 못하는 동작과 성능 이슈
 *  
 */
console.log('-'.repeat(20));
console.log('[Number() 로 생성하기]');

num1 = 123;  // number
num2 = new Number(123); // Number 객체 (object)
num3 = new Number(123);
console.log(num1, num2, num3);
console.log(num1 + num2);  // number + Number객체
console.log(typeof (num1), typeof (num2)); // number object

console.log(num1 == num2);  // true
console.log(num1 === num2);  // false

// object 끼리의 비교연산은 언제나 false
console.log(num2 == num3);  // false
console.log(num2 === num3);  // false
console.log({ name: '김정준' } == { name: '김정준' });  // false

num4 = num3;  // 주소값 대입
console.log(num4 == num3);  // true  주소값 비교 (동일성 비교)


/*********************************
 * Number 의 메소드(method) 들 
 */
console.log('-'.repeat(20));
console.log('[Number 의 메소드들]');


// toFixed(n)
//  소숫점 이하 n자리까지 표현한 '문자열' 결과  (이하 반올림)
//  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed

num1 = Math.PI;

console.log(num1);
console.log(num1.toFixed(2));  // "3.14"  결과는 string 타입
console.log(num1.toFixed(3));

// toExponential() 메서드는 숫자를 지수 표기법으로 표기해 반환합니다.
//  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/toExponential




// toPrecision(n)
//  Number 객체를 지정된 정밀도로 나타내는 문자열을 반환한다.
//  n : 유효 자릿수
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/toPrecision




/****************************************
 * number 로 변환하는 방법 4가지
 *
 *  Number() '함수'
 *  parseInt()
 *  parseFloat()
 *  + / - 부호 붙이기
 *
 *  다양한 경우에서 사용자가 입력한 값은 문자열(string) 타입으로 입력된다
 * 이의 산술연산을 하거나 Number 메소드를 적용하려면 number로 변환해야 한다
 */
console.log('-'.repeat(20));
console.log('Number 변환하기');
num1 = "3.141592";

// num1.toFixed(2);
console.log(parseFloat(num1));
console.log(parseInt(num1));
console.log(parseFloat(num1).toFixed(2));

console.log(parseInt("10년")); // 10
console.log(Number("10"));  // 10  <- number 타입

console.log(Number(true));
console.log(Number(false));

console.log(+"10");   // 10 number
console.log(-"10");   // 10 number



/***********************************
 * Number 의 property
 *   https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number#static_properties
 *
 * Number 의 static 메소드
 *   https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number#%EC%A0%95%EC%A0%81_%EB%A9%94%EC%86%8C%EB%93%9C
 */
//  console.log('-'.repeat(20));
//  console.log('Number 의 property, static 메소드');






