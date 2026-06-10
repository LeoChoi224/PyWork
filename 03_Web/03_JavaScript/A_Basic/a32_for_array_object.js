/****************************************
 * JS 는 for 가 복잡하게 많다.
 * 
 * 배열, object, string 과 for
 *  for, for~in, for~of, forEach
 */
console.log("[for, for~in, for~of, forEach]");

const points = [40, 100, 1, 5, 25, 10];
const fruits = ["Banana", "Orange", "Apple", "Mango"];
const cars = ["Saab", "Volvo", "BMW"];
let arr1, arr2;

/***********************************
 * for 사용
 * object 의 property 에 대한 접근 횟수를 줄이는게
 * 성능에 유리하다.
 */

let i
for (i = 0; i < cars.length; i++) {
    console.log(cars[i]);
}

/*************************************
 * for ( .. in .. ) 
 *   'property(key/인덱스)' 를 반복한다.  
 *    주로 '객체(object)' 에 대해 사용
 */
console.log("-".repeat(20));
console.log('[for(  in  )');
obj = {name: 'John', age: 15, gender: 'male'};

for(x in obj){
    console.log(`${x} : ${obj[x]}`);
}


/************************************
 * for (  of   )  
 *   value 에 대해 순환
 *   ES6 에 등장
 *   iterable 한 객체에 사용가능  (아래 추가 설명)
 *   https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/for...of
 */
console.log("-".repeat(20));
console.log('[for(  of  )]');

for(item of fruits){
    console.log(item);
}

/***********************************
 * 배열.forEach(함수)
 *  배열원소를 하나하나 뽑아내면서 함수가호출되어 실행 (이런식으로 되호출되는 함수를 callback 함수라 한다)
 *  이때의 callback 함수
 * 		매개변수는 (value, index, array)
 * 
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
 */
console.log("-".repeat(20));
console.log('[배열.forEach(함수)]');

// 이름 있는 함수
function myFunction(value){
    console.log('🐹', value);
}

console.log(fruits);
fruits.forEach(myFunction);

console.log('-'.repeat(20));

// 이름 없는 함수
fruits.forEach(function(v){
    console.log('🐷', v);
});

console.log('-'.repeat(20));

// 화살표 함수
fruits.forEach(e => console.log('🐶', e));

// callback 함수의 매개변수 확인
fruits.forEach(function(){});

// callback 함수의 매개변수 확인
fruits.forEach(function(value, index, array){
    console.log('🎃', index, value, array);
});

// 도전: 주어진 배열의 값을 x2 한 배열 구하기
// 결과: [ 80, 200, 2, 10, 50, 20 ]
console.log('points =', points);
result = []
points.forEach(n => result.push(n * 2))
console.log(result)

result = []
for(num of points) {
    result.push(num * 2)
}
console.log(result)

// 도전: 주어진 배열중 짝수만 담긴 배열 구하기
// 결과: [ 40, 100, 10 ]
console.log('points =', points);
result = []
points.forEach(n => n % 2 == 0 && result.push(n))
console.log(result)

result = []
for(num of points) {
    num % 2 == 0 && result.push(num)
}
console.log(result)


/********************************
 * for~in 과 object
 *  for(property in object)
 * 
 * 	object 에서 for~of 는 사용 못함
 * 	
 * 	for~of 는 iterable 한 객체에 대해서만 사용 가능.
 */
console.log("-".repeat(20));
console.log('[object 순환문]');

const person = {
	firstname : "John",
	lastname : "Doe",
	age : 50,
	eyecolor : "blue"
};

// 따라서! object 를 순환(iteration) 할 경우
// ↓아래 3가지를 활용하도록 하자 (ES2017 에 등장)
//  아래 결과에 forEach() 나 for~of 적용 가능

// 위 object 의 key 들만 뽑아내려면?
console.log(Object.keys(person)); // 배열

// 위 object 의 value 들만 뽑아내려면?
console.log(Object.values(person)); // 배열

// 위 object 의 [key, value] 를 뽑아내려면?
console.log(Object.entries(person)); // 2차원 배열

for(e of Object.entries(person)){
    console.log('🤪', e[0], e[1]);
}

console.log();

// 비구조화 할당 구문 사용.
for([k, v] of Object.entries(person)){
    console.log('💙', k, v);
}


/****************************************
 * string 
 * 	 for, for~in, for~of, 
 * 
 * 	 string 은 iterable 하기 때문에 for~of 사용 가능
 */
console.log("-".repeat(20));
console.log('[string 과 for]');
const str = "Hello";

for(ch of str){
    console.log('🌐', ch);
}

// forEach() 는 배열의 함수다!
// str.forEach(ch => console.log(ch));

str.split("").forEach(ch => console.log('🟡',ch));


/***********************************************
 * iterable
 * 
 * JS 에서 배열과 같이 for ~ of 로 순환할수 있는 객체를 iterable 이라 한다.
 * 
 * JS 의 기본 내장 iterable 은 
 *  String, Array, TypedArray, Map, Set
 * 
 * ★DOM 객체에 대해서도 얼마든지 사용 가능.
 *   ex) getElementsByTagName()
 * 
 * 그 밖에도 얼마든지 사용자 정의 iterable 객체 정의 가능
 * 
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Iteration_protocols
 * 
 * (이는 고급 주제이므로 기회가 되면 다루겠습니다)
 */
