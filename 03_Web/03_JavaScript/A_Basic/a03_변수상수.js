/*
    변수 (variable)
        값을 담는 공간.  변수이름(variable name)을 부여해서 관리    

      변수는 사용하기 전에 먼저 '선언(declaration)' 해야 한다
	
     변수 선언 구문 방법 4가지:
        ● let 변수이름    ← let 으로 선언된 변수는 값 변경 가능
        ● const 변수이름  ← const 로 선언된 변수는 값 변경 불가. 이는 상수(constant) 라 한다. 반드시 선언시 초기화 해야 한다
        ● var 변수이름    ← var 키워드는 오늘날 JS 에서는 가급적 사용하지 않음.  값 변경 가능
        ● 걍 변수이름..

    변수에 값을 대입 (assign)
         =  대입연산자 (assignment operator) 사용

    변수의 초기화 (initialization)
        변수에 최초로 값(value) 을 대입 (assignment) 하는 것.

    타입 확인
        모든 값이나 변수는 타입(type) 과 값(value) 을 갖고 있다.
        typeof 연산자를 통해 타입 확인 가능.

    변수 이름
        변수 이름은 고유한 식별자 (identifier)로 작명해야 한다
        - 문자, 숫자, _, $ 사용 가능
        - 숫자로 시작하면 안된다
        - 대소문자 구분한다  (case sensitive)
        - 예약어 (reserved word), 키워드는 변수명으로 사용 불가

    
    가급적 코드에서 사용하는 모든 변수들은 코드의 상단에서 선언해두자.
*/

let num1;
num1 = 20;
console.log('num1 =', num1);

let num2;
console.log('num2 =', num2);  // undefined!

console.log('-'.repeat(20));
// typeof 연산자
console.log(typeof 10);   // number
console.log(typeof "10");  // string
console.log(typeof (10), typeof ("10"))

// 사용가능한 변수명
let abc;
let year2022;
let $;  // $ 를 사용 가능!
let $$$;
let $myMoney;
let _name_;

// 사용불가능한 변수명
// let 9monkey;    // 숫자
// let my name;  // 띄어쓰기
// let function;  // 키워드
// let num1;  // 중복된 이름의 변수 선언 불가 (let, const 의 경우)

// 상수
const PI = 3.14
console.log('PI =', PI);
// PI = 123;  // 상수 값 변경불가!

// var 는 중복 선언 가능
var k = 10;
var k = 20;


// 키워드 없이 선언 가능  --> global
// delete 로 삭제 가능.
myValue = 200;
console.log(myValue);
delete myValue;   // 변수 삭제
// console.log(myValue);

//  두 변수 값 바꾸는 방법
console.log('-'.repeat(20))
console.log('[두 변수 값 바꾸기]')
num3 = 100;
num4 = 200;
let temp;

console.log("바꾸기전 num3=" + num3 + " num4=" + num4);
temp = num3;
num3 = num4;
num4 = temp;
console.log("바꾼후 num3=" + num3 + " num4=" + num4);

// ES6 부터 등장한 비구조화 할당 구문을 사용하여
// 아래와 같이 편리하게 두개 변수값 서로 교환 가능
// ※ 해당 단원에서 다시 다룰께요.
// ※ 참고로 위의 문장끝 ; 를 빼면 아래에서 에러 난다 (경험해보세요)

// num3, num4 = num4, num3
[num3, num4] = [num4, num3];
console.log("바꾼후 num3=" + num3 + " num4=" + num4);

/*
* let, const 는 block scope (블럭 영역) 를 갖는 변수다
*   블럭 안에서 선언된 변수는 선언이후 블럭안에서만 사용가능함
*   블럭이 끝나면 해당 이름의 변수는 사용 불가
*  
*   이러한 변수를 지역변수(local variable) 이라 하고
*    local scope (지역 범위) 를 갖는다 라고 말합니다.
*    scope 는 해당 이름을 사용할수 있는 범위
*/
{
    let i = 100;
    // j = 200;
    console.log('i =', i);
}
// console.log('i =', i);
// console.log('j =', j);

let age = 1;
let grade = 4;
{
    let age = 2;
    console.log('age.2 =', age);
    console.log('grade.2 =', grade); // 블럭 바깥쪽 변수 사용 가능
}

console.log('age.1 =', age);


