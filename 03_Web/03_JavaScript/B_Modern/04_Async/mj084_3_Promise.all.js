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

  // TODO
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

  // TODO
}
