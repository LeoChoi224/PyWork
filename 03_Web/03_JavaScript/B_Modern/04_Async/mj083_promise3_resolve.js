// Promise 를 사용하여 callback hell 을 벗어나자
// ex)
// const myPromise = new Promise((resolve, reject) => {
//      구현..
// })
// Promise 는 성공 할 수도 있고, 실패 할 수도 있습니다.
// 성공 할 때에는 resolve 를 호출해주면 되고,
// 실패할 때에는 reject 를 호출해주면 됩니다.
//     https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise

//  실패하는 상황은 고려하지 않고,
// 몇초 뒤에 성공시키는 상황에 대해서만 구현을 해보겠습니다.
//  성공하는 경우 resolve() 수행

{
  console.log("Promise() + resolve 사용");

  const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();  // TODO: resolve(값) -> then(callback) 에 전달됨.
    }, 6000);
  });

  myPromise.then(() => {  // TODO
    console.log("then() :");
  });

  console.log("다음 작업...")
}
