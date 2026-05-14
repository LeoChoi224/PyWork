/**********************************
 * 배열 정렬 sort()
 *  
 *  sort() : 매개변수 없으면 배열 각 요소를 '문자열변환'하여 문자열 비교 진행
 *  sort(비교함수) : 비교함수가 있으면 비교함수의 리턴값에 따라 정렬.
 * 
 *  리턴값: sort() 는 원본 변경 발생한다 ★ 그렇게 정렬된 배열이 리턴된다. 
 *     (새로운 배열이 만들어지는게 아니다)
 * 
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
 */
let points = [40, 100, 1, 5, 25, 10];
let fruits = ["Banana", "Orange", "Apple", "Mango"];
let cars = ["Saab", "Volvo", "BMW"];

 console.log('-'.repeat(20));
 console.log("sort()");
 console.log(fruits);
 
 fruits.sort();   // 원본을 변경함
 console.log(fruits);
 
 // 역정렬하려면?
 console.log(cars);
 console.log(cars.sort());  // 오름차순
 console.log(cars.sort().reverse()); // 내림차순
 
 
 // 숫자 데이터 정렬할때는 어케 될까?
 let arr1 = [40, 100, 1, 5, 25, 10];
arr1.sort();
console.log(arr1);  // 잉?    [ 1, 10, 100, 25, 40, 5 ]

// 뭔가 제대로 안된다.
// sort() 메소드는 기본적으로 문자열(string) 정렬을 합니다
// 그래서 "25" 가 "100" 보다 더 큰 값이 되는 겁니다
// 따라서 number 타입등에서 sort() 할때는
// '비교함수'를 sort() 의 매개변수로 주어 동작케 해야 합니다
// 
//  '정렬(sort)' 알고리즘은 내부적으로 '비교' 연산을 여러번 합니다
//  바로 그 '비교연산' 을 수행하는 함수를 전달해주는 겁니다
// 
//   비교함수(compare function)는 두개의 값의 '대소'를 비교할수 있도록 동작하면 됩니다
//     매개변수: 비교할 두개값 a, b
//     리턴값은: 
//        a 보다 b 가 크면 '양수' 리턴
//        a 보다 b 가 작으면 '음수' 리턴
//        a ,b 가 같으면 '0' 을 리턴
//    위와같이만 동작하도록 정의하여 sort() 에 전달해주면 됩니다.
//    그러면 나머지는 sort() 가 알아서 동작합니다

arr1.sort((a, b) => a - b);  // 오름차순 
console.log(arr1);

arr1.sort((a, b) => b - a);  // 내림차순 
console.log(arr1);

//-------------------------------------------------------------------------------
console.log('-'.repeat(20));
arr1 = [
    {
        name: 'James',
        age: 34,
        score: [100, 89, 88],
    },
    {
        name: 'Amy',
        age: 41,
        score: [56, 13, 97],
    },
    {
        name: 'Kevin',
        age: 23,
        score: [96, 88, 59],
    },
]
console.log(arr1);

// 이름 오름차순
console.log('이름 오름차순');
arr1.sort((a, b) => {
    if(a.name < b.name) return -1;
    if(a.name > b.name) return 1;
    return 0;
});
console.log(arr1);

// 이름 내림차순
console.log('이름 오름차순');
arr1.sort((a, b) => {
    if(a.name < b.name) return 1;
    if(a.name > b.name) return -1;
    return 0;
});
console.log(arr1);

// 나이 오름 차순 정렬
console.log('나이 오름차순 정렬');
arr1.sort((a, b) => a.age - b.age);
console.log(arr1);

// 나이 내림 차순 정렬
console.log('나이 내림차순 정렬');
arr1.sort((a, b) => a.age < b.age ? 1 : -1);
console.log(arr1);

// 총점 오름 차순 정렬
console.log('총점 오름차순 정렬');
arr1.sort(function (a, b) {
    return a.score.reduce((a, b) => a + b) - b.score.reduce((a, b) => a + b);
});
console.log(arr1);

// 총점 내림 차순 정렬
console.log('총점 내림차순 정렬');
arr1.sort(function (a, b) {
    return -(a.score.reduce((a, b) => a + b) - b.score.reduce((a, b) => a + b));
});
console.log(arr1);

