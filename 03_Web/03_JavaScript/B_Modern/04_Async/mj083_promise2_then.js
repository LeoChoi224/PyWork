/*
    'then 을 설정하는 시점'을 정확히 하고,
    함수의 실행과 동시에 Promise 객체를 만들면서
    pending 이 시작하도록 하기 위해
    Promise 객체를 생성하면서 리턴하는 함수 (p) 를 만들어
    함수 (p) 실행과 동시에 then 을 설정합니다.
*/
{
  function p() {
    return new Promise((resolve, reject) => {
      console.log('p() Promise 생성 : pending 상태'); // pending 상태

      setTimeout(() => {
        console.log('p() Promise fulfilled 전환');
        resolve();   //  fulfilled 상태로 전환
      }, 2000);
    });
  }

  // TODO

  // console.log("Promise 완료");
}
