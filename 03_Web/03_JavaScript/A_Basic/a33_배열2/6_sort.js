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
 



console.log("\n[프로그램 종료]", '\n'.repeat(20));




















