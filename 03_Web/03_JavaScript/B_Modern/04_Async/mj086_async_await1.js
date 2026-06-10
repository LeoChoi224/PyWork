/*
. async/await
    ES8 (ECMA2017) 부터 등장한 문법  ** 비록 ECMS2017 의 문법이지만, 매우 중요합니다!
    Promise 를 더욱 쉽게 사용

    [사용법]
        async function 함수이름() {}
        const 함수이름 = async() => {}

    https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/async_function
    https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/await
*/

// ※ Eclipse Web Developer 는 ES8 지원 안함 ..

{
    // Promise 객체를 리턴하는 함수
    function p(ms) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                return resolve(ms);
            }, ms);
        })
    }

    // Promise 객체를 이용해서 비동기 로직을 수행할때
    console.log("p() 시작");
    p(1000).then(ms => console.log(`시작후 ${ms}ms 후에 실행됨`))
    console.log('다음작업');

    // 위 동작을 async await 로 하게 되면...↓

    // 'Promise 객체를 리턴하는 함수'를 await 로 호출하게 되면
    // .then() 으로 연결하지 않아도
    // 정상적으로 p() 가 종료할때까지 기다린후 다음이 실행된다.
    // ms 가 리턴값으로 나옴!
    const ms = await p(2000);
    console.log(`${ms} ms 후에 실행`);
    // 그러나 ↑ 원래 이건 에러다 ! --> SyntaxError: await is only valid in async function
    // ★await 를 사용하는 경우, 항상 async 함수 안에서 사용되어야 한다.

    // ※ 단 최근 node.js 에선 '톱레벨 await(top-level await)' 이라 하여
    // 모듈 최상위(top-level)에서 async 함수 없이도 await를 쓸 수 있긴 하다.


}