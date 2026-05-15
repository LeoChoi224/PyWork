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
    // TODO


}