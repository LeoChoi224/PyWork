/*
  동기 vs 비동기

  이런 작업들을 비동기로 처리한다
  Ajax Web API 요청: 만약 서버쪽에서 데이터를 받와아야 할 때는, 
    '요청(request)' 을 하고 서버에서 '응답(response)'을 할 때 까지 
    대기를 해야 하는데, 
    이 대기 시간이 긴 경우 이와 같은 작업을 비동기적으로 처리합니다.
  ex)
    파일 읽기: 주로 서버 쪽에서 파일을 읽어야 하는 상황
    암호화/복호화: 이 또한 시간이 어느정도 걸리는 경우가 있다.
    작업 예약: 단순히 어떤 작업을 몇초 후에 스케쥴링 해야 하는 상황
              setTimeout 을 사용하여 비동기적으로 처리합니다
*/

console.log("동기화된 작업(기본)");
{
  function work() {
    // 아래의 for문이 수행되는 경과시간 측정하기
    const start = Date.now(); // 현재날짜->Timestemp (ms)
    for (let i = 0; i < 1000000000; i++) { }
    const end = Date.now(); // 현재날짜 -> Timestamp (ms)
    console.log("[A] 작업 종료", end - start + "ms");
  }

  console.log("[A]", "작업 시작!");
  work();
  console.log("[A]", "다음 작업"); // 위의 work() 가 끝난 다음에야 이 라인이 수행됨.
}

console.log();

// setTimeout(func, [delay(ms)])
// 주어진 함수를 비동기로 진행
//   setTimeout(함수, 경과시간ms)
//    https://developer.mozilla.org/ko/docs/Web/API/WindowTimers/setTimeout

console.log("🟦 비동기. setTimeout() 사용");
{
  function work() {
    setTimeout(() => {
      const start = Date.now();
      for (let i = 0; i < 1000000000; i++) { }
      const end = Date.now();
      console.log("[B3] 작업 종료", end - start + "ms");
    }, 0);
    console.log('[B4] work() 종료');
  }

  console.log("[B1]", "작업 시작!");
  work();
  console.log("[B2]", "다음 작업");
}

console.log();

/*
work 함수의 비동기작업이 끝난 다음에 어떤 작업을 처리하고 싶다면 어떻게 해야 할까요? 
 이럴 땐, 콜백 함수를 파라미터로 전달해주면 됩니다. 
 콜백 함수란, 함수 타입의 값을 파라미터로 넘겨줘서, 
 파라미터로 받은 함수를 특정 작업이 끝나고 호출을 해주는 것을 의미합니다.
 */
// console.log("비동기 작업후. callback() 지정하기");
{
  // 비동기 작업이 끝난후 실행할 콜백함수를 매개변수로 받는다

  function work(callback) {
    setTimeout(()=>{
      const start = Date.now();
      for (let i = 0; i < 1000000000; i++) { }
      const end = Date.now();
      console.log("[C3] 작업 종료", end - start + "ms");

      callback(end-start);  // 비동기 작업 끝나고 수행.
    
    }, 0);
    console.log('[C4] work() 종료');
  }

  console.log("[C1]", "작업 시작!");
  work(ms => {   // work 호출하여, 비동기 작업 끝나고 수행할 함수 전달
    console.log(`[C5] ${ms}ms 작업완료후 진행한 callback`);
  });
  console.log("[C2]", "다음 작업");
}