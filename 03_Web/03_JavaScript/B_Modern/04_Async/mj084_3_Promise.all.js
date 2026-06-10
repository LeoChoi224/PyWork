/*
  Promise.all([Promise 객체들])
    Promise 객체 여러개를 생성하여,
    배열로 만들어 인자로 넣고, Promise.all 을 실행하면
    배열의 '모든 Promise 객체' 들이 fulfilled 되었을때, then 의 함수가 실행됩니다.
    then 의 함수의 인자로 Promise 객체들의 resolve 인자값을 배열로 돌려줍니다.


    https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/all
*/

{
  function p1(ms) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`p1 ${ms}ms 작업 fulfilled`);
            resolve()
        }, ms);
    })
  }

  let start = Date.now();
  Promise.all([p1(1000), p1(2000), p1(3000)]).then(() => {
    console.log(`p1] 모두 fulfilled 됨. 경과시간 ${Date.now() - start}ms`);
  })
}

{
  function p2(ms) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // resolve() 에 인자 넘어 보내기
            resolve(ms)
        }, ms);
    })
  }

  Promise.all([p2(4000), p2(5000), p2(6000)]).then(messages => {
    // messages: 위 resolve(value) 들의 value 값(들)의 배열
    console.log()
    console.log(`p2] 모두 fulfilled 된 이후`, messages);})
}
