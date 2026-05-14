/***************************************
 *  배열의 메소드 filter(판별함수)
 *   특정조건(판별)을 만족하는 원소들만으로 새로운 배열 생성
 *   매개변수로 주어지는 판별함수는 Truthy/Falsy 를 리턴해야 한다
 *   배열원소가 판별함수에 주어시고 Truthy 가 리턴되면
 *   새로운 배열에 추가된다.
 * 
 *  리턴값: 그렇게 걸러져 나온 원소들이 담긴 배열
 * 
 * ES5 등장
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
 */

let array = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// 위 배열에서 3의배수만 걸러진 배열을 구하려면?
//          [1, 2, 3,  4,  5,  6,  7,  8,  9]
// 3의배수?  x  x  ↓   x   x   ↓   x   x   ↓
//          [      3           6           9]


console.log(array.filter(e => e % 3 == 0));

// --------------------------------------------

let todos = [
    {
        id: 1,
        text: "자바스크립트 입문",
        done: true
    },
    {
        id: 2,
        text: "함수 배우기",
        done: true
    },
    {
        id: 3,
        text: "객체와 배열 배우기",
        done: true
    },
    {
        id: 4,
        text: "배열 내장함수 배우기",
        done: false
    }
];

//

// done 값이 false 인 것만 뽑아내려면 (filtering!)
// ==> [ { id: 4, text: '배열 내장함수 배우기', done: false } ]


// for ~ of 사용 
arr = [];
for (todo of todos) {
    todo.done || arr.push(todo)
};
console.log(arr);

// forEach 사용
arr = [];
todos.forEach(todo => todo.done || arr.push(todo));
console.log(arr);

// filter 
console.log(todos.filter(todo => todo.done === false));