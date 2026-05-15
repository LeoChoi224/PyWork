// Promise.all() 을 사용하지 않은 경우
// 여러개의 비동기 함수를 몇개 더 만들어 실행하면
{
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // TODO
}
