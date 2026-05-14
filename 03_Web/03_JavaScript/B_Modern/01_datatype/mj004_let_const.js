// JavaScript 는 선언문으로 
// var, let, const 3가지가 있다.


// 변수 선언, 여전히 var 사용 가능.
var v1 = 100;
console.log('v1 =', v1)

v2 = 200;   // var 없이도 선언은 가능.
console.log(`v2 = ${v2}`)

var v1 = 300;   // 동일 이름의 변수 중복 선언 가능.
console.log(`v1 = ${v1}`)

// ★ var 는 '오늘날 js' 에서는 그닥 권장하지 않습니다.

/*
   ES6 부터 let, const 소개.  (IE9, IE10 와 같은 구형브라우저는 지원안함)
    변수 선언 --> let
    상수 선언 --> const  


    let 
        동일이름 변수 중복 선언 불가
        https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let
            ↑ 처음이라면 함 보자.

    const
        한번 선언 + 초기화 하면 값 변경 불가.
        https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const

    이들은 block scope 를 가진다.
        { ... }
*/

let value = 177
console.log(`value = ${value}`);

// TODO

//────────────────────────────────────────────────────────────────────


