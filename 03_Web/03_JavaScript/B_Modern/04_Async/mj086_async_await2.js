{
  // 아래 코드 수행시 화면에 찍히는 순서들을 잘 보고, 생각해보자

  function p1(ms) {
    // Promise 를 리턴하는 함수를 await 로 사용 가능
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        console.log('p1_1] Promise fulfilled 작업완료');
        return resolve(ms);
      }, ms);
    });
  }

  async function main() {
    console.log(`p1_2] 1000ms 기다기리 시작`)
    const ms = await p1(1000);   // resolve(값) 의 값 이 리턴
    console.log(`p1_3] 실행완료 ${ms}ms 후`)
  }

  p = main();
  console.log('p =', p);  // async 함수 호출 결과는 Promise 객체
  console.log(`p1_4] main 다음 작업`);


}
{
  function p2(ms) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        return resolve(ms);
      }, ms);
    });
  }

  // TODO
}

// Promise 객체가 rejected 된 경우의 처리를 위해
// try catch 를 이용한다.
{
  function p3(ms) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        // return resolve(ms);  // 정상적으로 끝나면
        console.log('p3_1] Promise rejected 됨');
        reject(new Error('💢이유이유')); // 에러가 발생하면
      }, ms);
    })
  }

  (async function () {
    try {
      console.log(`p3_2] 3000ms 기다리기 시작`);
      const ms = await p3(3000);  // 정상적으로 끝나면 .. 
      console.log(`p3_3] 실행완료 ${ms} ms 후`)
    } catch(error) {  // reject(reason) 의 reason이 넘어온다
      console.log(`p3_4] catch: `, error.message);
    }
  })();

  console.log(`p3_5] 다음 작업으로...`)
}

// async function 에서 return 되는 값은
// Promise.resolve 함수로 감싸서 리턴된다.
{
  function p4(ms) {
    // Promise 를 리턴하는 함수를 await 로 사용 가능
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        return resolve(ms);  // 정상적으로 끝나면
        // reject(new Error('이유이유')); // 에러가 발생하면
      }, ms);
    })
  }

  // TODO

}
