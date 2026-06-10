/*
    Template Literal 문법 (ES6 등장)  -> ※Python 의 f-string
    ES6 에는 문자열 조합을
    편리하게 할수 있는 방법 제공
        '이전에는 Template String이라 불렸지만
        'ES2015 명세서 부터는 Template Literal 이라 부름
    
    backtick (`) 문자 사용한 문자열 포맷팅
        문자열 안에서 ${변수}
        문자열 안에서 ${값}
        ..

    공식]
        https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Template_literals        

    이와같이 불리기도 한다]
        Template Literals
        Template Strings
        String Templates
        Back-Tick Syntax
*/

let x;
x = '김정준';
console.log('Hello, ' + x + "!");
console.log(`Hello, ${x}!`);

// 리터럴내 줄바꿈도 가능
x = `동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라만세`;
console.log(x);

//-------------------------------------------------
x = {name: "John", age: 40};
console.log(x)  // { name: 'John', age: 40 }
            // {key: 'value' } <-- console.log() 는 object '단독' 출력시 이쁘게 '출력'해준다
            //   절.대.로 toString() 의 결과값이 아닙니다.  (※ 파이썬의 __str__() 에 해당하는게 toString() )

// print(x) <-- x 의 무슨값?  __str__

console.log('x = ', x);
console.log('x = ' + x);  // "[object Object]"  <- x.toString()
console.log(x.toString());
console.log(`x = ${x}`);
            // template literal 도 내부적으로 문자열 연결연산(+)  
            // => 'x = ' + x.toString()
