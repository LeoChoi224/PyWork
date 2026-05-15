// Promise.race() 는
// Promise 들중 하나라도 성공하면 나머지에 실패가 발생하도
// Promise.race() 가 실패한것으로 간주하지 않습니다.
// 하필 가장 먼저 끝난게 에러 발생하면 Promice.race() 는
// 에러로 간주합니다.
{
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }


    // TODO

}