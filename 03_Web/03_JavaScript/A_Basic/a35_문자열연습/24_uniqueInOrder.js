/*******************************
 * 
 */

const input = [
    "all good tree", // ['a', 'l', ' ', 'g', 'o', 'd', ' ', 't', 'r', 'e']
    "AAA AAAA AA AAA",  // ['A', ' ', 'A' ,' ', 'A', ' ', 'A']
    "i AM a BOY",  // ['i', ' ', 'A', 'M',' ', 'a', ' ', 'B', 'O', 'Y']

    // 다른 입력 데이터로 테스트 필요하면, 배열에 데이터 더 넣어보고 실행해도 됩니다
]

function uniqueInOrder(str) {
    arr = [];
    idx = 0;
    str.trim().split("").forEach(ch => {
        if (arr[idx - 1] != ch) { // 처음 undefined 와 비교 에러 x
            arr.push(ch) && idx++;
        }
    });

    return arr;
}

input.forEach(e => console.log(uniqueInOrder(e)));


// ueInOrder(str) {
//     arr = [];
//     idx = 0;
//     str.trim().split("").forEach(ch => {
//         if (idx) {
//             arr[idx - 1] != ch && arr.push(ch) && idx++;
//         } else {
//             arr.push(ch);
//             idx++;
//         }
//     });

//     return arr;
// }
// arr2 = [];

// console.log(arr2[-1])
// console.log(arr2[-1] == "a")