// 연속된 Promise 의 처리와 
// 연속된 async await 
// 두가지 비교해보자.

{

    function p(ms){
        return new Promise((resolve, reject) => {
            setTimeout(() => {
               resolve(ms);
            }, ms);
        })
    }

    // TODO

}
