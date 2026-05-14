console.log('\n-- Scope --')
/*
    자바스크립트의 Scope : 변수 가 유효한 범위
    JS 의 Scope 는 총 3가지

    Global (전역) Scope: 코드의 모든 범위에서 사용 가능
    Function (함수) Scope: 함수 안에서만 사용 가능
    Block (블록) Scope: if, for, switch 등 특정 블록 내부에서만 사용 가능

    let, const 는 block scope 
    var 는 function scope

    ES6 부터 등장한 const, let 를 더 선호하는 이유 (추천)
        function scope 보다는 
        block scope 가 훨~씬 직관적이기 때문!

    ※ 단. 기존 (과거의) 코드, 라이브러리를 사용하는 경우가 있슴
*/

// 블럭 외부에서 선언
const outer1 = 100
let outer2 = 200
var outer3 = 300
outer4 = 400

// 블럭
{
    console.log("블럭안") 

    // TODO
}


//────────────────────────────────────────────────────────────────────


