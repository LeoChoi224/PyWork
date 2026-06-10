/*
    Promise.race([Promise 객체들]);

    Promise 객체를 여러개를 생성하여
    배열로 만들어 인자로 넣고, Promise.race 를 실행하면,
    배열의 모든 Promise 객체들 중 '가장 먼저' fullfilled 된 것으로,
    then 의 함수가 실행됩니다.
    then 의 함수의 인자로 가장 먼저 fulfilled 된 Promise 객체의
    resolve 인자값을 돌려줍니다.

    https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/race
*/

{
    function p(ms) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                // resolve() 에 인자 넘어 보내기
                resolve(ms)
            }, ms);
        })
    }

    let start = Date.now()
    Promise.race([p(7000), p(8000), p(9000)]).then((message) => {  // message <- 가장 먼저 끝난 '한개' 의 resolve(value) 의 value 값이 전달됨
        console.log('가장 빨리 fulfilled 된 하나가 실행됩니다', message) // 출력해주기
        console.log('경과시간:', Date.now() - start) // 7초 경과!
    })

}

/*
    Promise 는 매우 중요!
    JavaScript 에서 비동기를 처리하기 위해..
    가장 기본이 되는 개념이 Promise !!

    다음에 배울 async, await 를 배우기 위해서도 알아두어야 한다.
*/
