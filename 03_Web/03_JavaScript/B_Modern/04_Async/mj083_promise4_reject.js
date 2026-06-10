/* reject, catch()

  실패하는 상황
  Promise 객체가 rejectd 되는 시점에 catch(callback) 안에 설정한
  callback 함수가 실행
  executor 의 reject 함수를 실행할때 '인자'를 넣어 실행하면,
  catch() 의 callback 함수의 '인자'로 받을 수 있습니다.
  
  reject('error');
  
  .catch((reason) => {...})

  ※ 일반적으로 자바스크립트의 Error 객체를 만들어서 넘겨주는게 일반적입니다
*/

{
  console.log("Promise() + reject 사용")

  const myPromise = new Promise((resolve, reject) => {
    console.log("Promise() 생성 : pending 상태")
    setTimeout(() => {
      // resolve("김정준")  // resolve(값)  이 값은 then의 callback 매개변수로 전달
      
      console.log("Promise : rejected 상태로 전환");
      reject(new Error("💥에러사유"));  // reject(값) 이 값은 catch의 callback 매개변수로 전달

    }, 4000);
  });

  myPromise
    .then(n => {console.log("then():", n)})
    .catch(e => {console.log("catch():", e.message)})
  
 
  // console.log("다음 작업...")
}