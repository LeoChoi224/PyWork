// 콜백함수를 많이 쓸때 왜 복잡해지 상황을 보자

// 숫자 n 을 파라미터로 받아와서
// 다섯번에 걸쳐 1초마다 1씩 더해서
// 출력하는 작업을 setTimeout 으로 구현
{
    function increaseAndPrint(n, callback) {
        setTimeout(() => {
            const increased = n + 1;
            console.log('🐹', increased);
            callback && callback(increased)
        }, 1000);  // 1초 뒤 실행 (delay)
    }

    increaseAndPrint(0, n => console.log("끝"));

    increaseAndPrint(0, n => {
        increaseAndPrint(n, n => {
            increaseAndPrint(n, n => {
                increaseAndPrint(n, n => {
                    increaseAndPrint(n, n => {
                        console.log('💥끝');
                    });
                });
            });
        });
    });
    // 비동기 호출이 많아질수록
    // 코드의 깊이(depth) 가 계속 깊어진다.
    // 즉 코드가 '아래'로 진행하지 않고 '안' 으로 깊어진다.

    // 작성하기도 어렵고, 보기도, 유지보수하기도 어렵다.
    // 이런 식의 코드를 Callback Hell (콜백지옥) 이라고 부릅니다.


    console.log("비동기 다음 작업 진행...")
}














  