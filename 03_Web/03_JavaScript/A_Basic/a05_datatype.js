/*
    JS의 자료형(data type) : https://www.w3schools.com/js/js_datatypes.asp
	
    타입
    https://www.w3schools.com/js/js_typeof.asp

        값을 갖고 있는 5개 타입
            number : 숫자 타입
            string : 문자열 타입
            boolean : 논리 타입 (true, false)        
            object : 객체 타입   => (python 의 dict 와 유사)
            function : 함수 타입

        6가지 object 타입
            Object : 객체
            Array : 배열         => (python 의 list 와 유사)
            Date
            String 
            Number
            Boolean

        값을 갖고 있지 않은 타입 2가지
            undefined : 타입이 지정되지 않음
            null : 데이터가 없는 object

        
    JS 는 dynamic type 을 지원하는 언어다.
*/

console.log('-'.repeat(20));
console.log('[number, string, undefined]');
let x;
console.log('x =', x, typeof (x));

x = 5;
console.log('x =', x, typeof (x));

x = "희준";
console.log('x =', x, typeof (x));

x = undefined;
console.log('x =', x, typeof (x));

// string + 숫자  연산에선 숫자를 "문자" 로 변환뒤 문자열 연결연산
x = "10" + 10;  // "1010" string
console.log('x =', x, typeof (x));

x = "10" * 10;   // 헐...
console.log('x =', x, typeof (x));

x = "10" - 10;   // 헐...
console.log('x =', x, typeof (x));

x = "10" / 10;   // 헐...
console.log('x =', x, typeof (x));

x = "10" > 2;   // 헐...
console.log('x =', x, typeof (x));

x = "10" > "2"   // false 문자열 비교 (코드값 비교)
console.log('x =', x, typeof (x));

x = "a" * 10;  // NaN : Not a Number
console.log('x =', x, typeof (x));

x = 10 / 0;     // Infinity
console.log('x =', x, typeof (x));



/*
* 배열 (array)   <- Python 의 list 에 해당
* 
* [ .. ]  bracket 으로 감싸고
* 그 안에 배열 원소(item) 들이 콤마로 나열됨. 
*/
console.log('-'.repeat(20));
console.log('array (배열)');

x = [10, 20, 30,]; // 맨 뒤 콤마 허용
console.log('x =', x, typeof (x));
console.log(x[0], x[1], x[2], x[3]);    // index 벗어나도 에러 아님!  undefined! 
console.log(x[-1]);  // 음수 인덱싱 지원안함. undefined
console.log(x.length);  // 배열 원소의 개수


/*
 * 오브젝트, 객체 (object)  --> ※ Python 의 dict 유사.
 * { .. }  curly brace 로 감싸고
 * name:value 쌍(property)이 콤마로 구분되어 나열됨.
 * name:value 쌍 을 object 의 property 라고 한다.
 */
console.log('-'.repeat(20))
console.log('[object (오브젝트)]')

x = { firstName: "John", lastName: "Doe", age: 50, eyeColor: "blue" };
console.log('x =', x, typeof (x));

console.log(x['firstName']);    // 방법1
console.log(x.firstName);    // 방법2
console.log(x.address);     // 없는 property name -> undefined
console.log(x.length);   // undefined


x = {
    'firstName': "John",
    10: "Doe",
    3.14: 50,
    true: "blue",
    // JavaScript 객체(Object)의 키(Key)는 기본적으로 '문자열' 또는 '심볼(Symbol)'입니다.
    // JavaScript 엔진은 이를 강제로 문자열로 변환하여 저장

};
console.log('x =', x, typeof (x));

x = null;
console.log('x =', x, typeof (x));

x = {};  // empty object
console.log('x =', x, typeof (x));

// undefined, NaN, null, Infinity 가 출력되고 있다면
// 무언가 잘못 만들어졌다는 뜻이다.