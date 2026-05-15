// Promise.all() 은 여러개 Promise 들 중에
// '하나라도' 에러가 발생하면 Promise.all() 전체가
// 에러가 발생 한것으로 간주함.

// Promise.all() 을 try ~ catch 로 감싼다

{
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }


    // TODO

}

