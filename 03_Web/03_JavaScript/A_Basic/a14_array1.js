/* 배열 array 타입
    여러개의 데이터를 담는 집합자료형
    
    array literal 은   [item1, item2, ...   ]  으로 만든다
    array 의 데이터(원소) 들은 , 콤마로 구분한다
    각 데이터(원소) 들은 어떠한 타입도 가능하다

    배열의 길이 (length)
 		배열 원소의 개수, 즉 배열에 담긴 데이터의 개수 
 		
 	배열 인덱스 (첨자, index)
 		배열의 인덱스는 0부터 시작해서, (배열의 길이 - 1)까지가 됨
 		배열인덱스를 사용하여 배열원소에 접근하여 사용


    배열변수는 일반적으로 const 로 선언한다.

    Array reference
    https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array
    https://www.w3schools.com/jsref/jsref_obj_array.asp
*/

// console.log('[왜 배열(array) 이 필요한가?]');

/****************************************
 * 배열생성 방법
 *  방법1 : [ ... ] 
 *  방법2 : new 사용
 */
// console.log('-'.repeat(20));
// console.log("[배열생성]");

// 배열생성 방법
// 방법1
let points = [40, 100, 1, 5, 25, 10];
let fruits = ["Banana", "Orange", "Apple", "Mango"];

// 방법2 : new 사용
let cars = new Array("Saab", "Volvo", "BMW");  // 비추

console.log(points);
console.log(points.toString());
console.log(typeof points); // object

arr1 = [10, 20, 30];
arr2 = [10, 20, 30];
console.log(arr1 == arr2);


// 일반적으로 배열변수는 const 로 선언한다



/********************************************
 * 배열 여부 판단 하기
 * 현재 객체가 배열인지 아닌지 판단
 * 
 * 방법1: Array.isArray() : 구 브라우저에서는 동작 안함  (ES5.1부터)
 * 방법2: constructor 사용 구 브라우저에서 동작시키려면 별도희 함수 만들어 사용
 * 방법3: instanceof 연산자 사용
 */
console.log('-'.repeat(20));
console.log("[배열여부 판단]");

// 방법1
console.log(Array.isArray(fruits));
const names = {
    0: "장희준",
    1: "김정준",
    2: "신하석", 
};

console.log(names[0], names[1], names[2]);
console.log(Array.isArray(names));  // false

// 방법2


// 방법3



/*****************************************
 * 배열원소, index, length
 *  배열의 원소를 사용하기 위해 index 사용
 *  배열 index 는 0 부터 시작 (0-base index)
 */
console.log('-'.repeat(20));
console.log('[배열원소, index, length]');

console.log(fruits.length);
console.log([].length);  // 0
console.log([10, 20, 30,].length);
console.log([  ,  ,10, 20, 30,  ,].length);
console.log([  ,  ,10, 20, 30,  ,]);
console.log([  ,  ,10, 20, 30,  ,][0]);  // undefined
/**************************************
 * 배열원소 추가, 제거
 *  push() : 배열끝 원소 추가, 새로운 length 리턴
 *  pop() : 배열 끝 원소 추출 (배열에서 제거 & 리턴). 추출할 원소가 없으면 undefined 리턴
 *  shift() : 배열 첫 원소 추출 (배열에서 제거 & 리턴). 추출할 원소가 없으면 undefined 리턴
 *  unshift() : 배열앞에 원소 추가, 새로운 length 리턴
 * 
 *  shift, unshift 는 pop, push 보다 성능이 느리다!
 */
console.log('-'.repeat())
console.log("[push() pop() shift() unshift()]");
console.log(fruits);

// 배열원수 추가방법1 (비추)
fruits[fruits.length] = "Melon";
console.log(fruits);

// fruits[10] = "김정준";  // 이유: 실수로 구멍(empty) 만들 수 있다
// console.log(fruits);

console.log('push() 결과', fruits.push("Grape"))
console.log('push() 이후', fruits)
console.log(fruits.length)

console.log('pop() 결과', fruits.pop());
console.log('pop() 이후', fruits);


/**************************************
 * 데이터 삭제, 삽입 splicing
 *  첫번째 매개변수 : 삭제할 데이터 위치 (start)
 *  두번째 매개변수 : 삭제될 데이터 개수 (deleteCount)
 *  세번째 이후 .. : 삽입될 데이터 들..
 *  리턴값: 삭제된 원소들의 배열. 원본변화됨
 */
console.log('-'.repeat(20));
console.log("데이터 삭제/삽입 splice()");
console.log(fruits);

fruits.splice(2, 0, "Kiwi", "Banana")
console.log(fruits);

fruits.splice(2, 3);
console.log(fruits);

console.log(fruits.splice(0, 1));
console.log(fruits);

// 주의! delete 를 사용하여 배열 원소 삭제 하지 말기
// 이는 배열에 구멍(undefined hole) 을 만들게 된다.
// delete 보다는 
// pop(), shift(), splice() 를 사용하길 권장

// delete fruits[1];
// console.log(fruits);

/**************************
 *  concat() 
 *    주어진 배열의 원소들을 추가, 원본변화 안함
 */
console.log('-'.repeat(20));
console.log("concat()");

console.log(fruits.concat(['Berry', 'Durian']));
console.log(fruits);


/*************************
 *  slice()
 * 배열의 일부분 추출, 원본에는 영향 안줌
 */
console.log('-'.repeat(20));
console.log("slice()");
console.log(fruits);

console.log(fruits.slice(1));
console.log(fruits.slice(1, 3));


/****************************
 * 원소 검색 indexOf(), includes()
 * 배열안에 특정 원소가 있는지 여부
 *  indexOf() : 찾으면 index 리턴, 못찾으면 -1 리턴
 *  includes() : 찾으면 true, 아니면 false 리턴, ES7(ES2016) 에 등장
 */
 console.log('-'.repeat(20));
 console.log("indexOf(), includes()");
 console.log(fruits);

console.log(fruits.indexOf("Mango"));
console.log(fruits.indexOf("Lemon"));

console.log(fruits.includes("Mango"));
console.log(fruits.includes("Lemon"));


/*************************************
 *  join() 
 *    array → string
 * 배열의 원소들을 주어진 문자열로 묶어서 하나의 문자열로 리턴
 */
// console.log('-'.repeat(20));
// console.log("[join()]");
// console.log(cars);

/******************************************
 * JavaScript 에선 array 도 object 의 특별한 형태다
 *  차이점이라면 index 의 형태다.
 *  JS 의 array : numbered index 사용
 *  JS 의 object : named index 사용
 */
console.log('-'.repeat(20));
arr1 = [];   // 비어있는 배열

arr1[0] = 100;
arr1[1] = 200;
console.log(arr1);

arr1[4] = 300;
console.log(arr1);
console.log(arr1.length); // 5
arr1['name'] = '신하석';
console.log(arr1);
console.log(arr1.length); // 5

/********************************
 * 배열 역순 reverse()
 *  원본 변화 발생.
 */
// console.log('-'.repeat(20));
// console.log("reverse()");
// console.log(cars);
 



/**********************************
 * 배열 정렬 sort()
 *  
 *  리턴값: sort() 는 원본 변경 발생한다 ★ 그렇게 정렬된 배열이 리턴된다. 
 *     (새로운 배열이 만들어지는게 아니다)
 * 
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
 */
 console.log('-'.repeat(20));
 console.log("sort()");
 console.log(fruits);

fruits.sort();   // 원본 변경
console.log(fruits); 

console.log(cars);
console.log(cars.sort());  // 원본을 변경하는게, 그 원본을 리턴까지 한다?

/**********************************
 * mutation(상태변경) 하는 메소드는 일반적으로 리턴값을 설정하지 않도록 설계하는 것이 좋으나,
 * JS 는 mutation 하고 리턴하는 메소드 설계가 많다 (위의 reverse(), sort() 처럼)
 * JS 는 mutation 에 대해 .. 일관적이지 않은 부분이 많다 ㅠㅠ.
 * 이는 프로그래밍 하면서 주의를 기울어야 하는 부분이다.
 * 가령..
 */
{
    const x = [1, 2, 3];
    const y = x.reverse();   // y=>[3, 2, 1]

    y.push(0);

    // x => ?
    // y => ?
    console.log('y =', y);
    console.log('x =', x);

    console.log(x == y);  // true : 동일객체다
    console.log(x === y);
}
