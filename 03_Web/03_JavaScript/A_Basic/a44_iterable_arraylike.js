/**
 * ■ 이터러블 (iterable) 객체  과 Array-like 객체
 * 
 * Iterable (이터러블) 객체
 *  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Iteration_protocols
 * 
 *  for ~ of 를 적용할 수 있는 객체를 이터러블(Iterable)이라 한다
 * 
 *  for ~ of 를 적용할 수 있으려면(즉 '이터러블' 이려면) (aka. iterable protocol)
 *     - 해당 객체는 Symbol.iterator() 이라는 메서드를 갖고 있어야 한다.
 *        for ~ of 에서 사용하려면 Symbol.iterator() 메서드가 호출된다.
 *          - 위 메서드는 'iterator object' 를 리턴해야 한다. 
 *          - 'iterator object' 는 next() 메서드를 갖고 있는 객체다.
 *          - next() 메서드를 호출하면 {done: Boolean, value: any} <- 이런 모양을 가진 object를 리턴해야 한다. 
 *             - done 프로퍼티 값이 true면 이터레이션이 끝난 것이고, 
 *               아니라면 value가 다음 value가 된다.
 * 
 *   참고
 *    https://javascript.info/iterable
 */

let range = {
    from: 1,
    to: 5,
};
for(let num of range){
    console.log(num);
}

/**
 * 'Array like 객체' 는  'numeric 인덱스' 와 '길이(length)' 가 있는 객체
 * 
 *   - Array like 객체가 Array 는 아니다!  push(), pop() 등의 Array 메소드가 없을 수 있다.
 *   - Array like 객체가 iterable 객체도 아니다!
 * 
 *   - Iterable 객체  와  Array-like 객체는 배타적이지 않다.
 *     array-like이면서 동시에 이터러블일 수 있다
 *     가령, string은 이터러블이면서 array-like 이다
 */

let arrayLike = { 0: "Hello", 1: "World", length: 2 }
console.log(Array.isArray(arrayLike));

// string은 이터러블이면서 array-like 이다
let str = "Hello";
console.log(Array.isArray(str));  // false  string 은 array 는 아니다.
console.log(str[0], str[1], str.length);  // string 은 array-like 객체다
for(ch of str){  // string 은 iterable 객체다
    console.log(ch);
}


/**
 * 기본적으로 Object 는 이터러블이 아니다. 
 * 그래서 직접적으로 for of를 사용할 수 없고, for of를 사용하려면 위에서 한 것처럼 
 * 직접 이터레이션 프로토콜을 이식해서 이터러블로 만들거나, 
 * Object.keys, Object.values, Object.entries 처럼 이터러블로 만들어주는 메서드를 사용해야 한다. 
 */

/**
 * Array.from()
 *   https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from
 * 
 *  '이터러블' 또는 'array-like' 을 인자로 받아서 진짜 Array로 바꿔주는 static 메소드
 *  Array.from(arrayLike or iterable[, mapFn[, thisArg]])
 *  두 번째 인자인 MapFn 은 배열의 모든 원소에 대해 호출될 매핑 함수.
 */

// str.forEach(ch => console.log(ch));
str.split("").forEach(ch => console.log(ch));

console.log();
Array.from(str).forEach(ch => console.log('🤪', ch));

console.log();
console.log(arrayLike);
console.log(Array.from(arrayLike));
Array.from(arrayLike).forEach(str => console.log(str.toUpperCase()));


