/*
    object

    property : value 쌍으로 구성된 데이터

    {property:value, property:value, ...}

    property 는 중복될수 없다.
    value 는 어떠한 타입도 될수 있다.
        : number, string, array, function, object..

    사실 JavaScript 의 모든 데이터의 실체는 object 이다.
    
    ※일반적으로  object 변수는 는 const 로 선언한다
    그러나 이번단원에서 진도 편의상 let 등을 사용하기도 하겠습니다
 */

let obj1, obj2, obj3, result;

const person = {
    firstName: "John",   // 관례적으로 : 다음에 띄어쓰기 한칸
    lastName: "Doe",
    age: 50,
    eyeColor: "blue",  // <- 마지막에 콤마 붙여도 에러 아님!
}

/* object 의 property 사용하기
    방법1 : objectName.propertyName
    방법2 : objectName["propertyName"] 
*/
console.log('-'.repeat(20));
console.log('[object 의 property]');

console.log('변경전', person);
person.firstName = 'Jane';
console.log('변경후', person);

person.email = 'jjj@mail.com';  // property 추가
console.log('추가후', person);

delete(person.email);
console.log('삭제후', person);

// person 을 const 로 선언 했는데 property 변경 가능?  
// person 을 바꾸지 못한다는 거지 person 의 property 를 변경 못한다는 게 아니다
// person = {name: 'hello'};   <-- person 값 자체를 변경하려 하면 이게 에러다!



/* value 는 어떠한 타입도 가능하다
*/
// console.log('-'.repeat(20));
// console.log('[object 의 value]');
/****************************************************
 *  object method 와 this
 * object 의 value 는 어떠한 타입도 가능하다
 * 즉, 함수도 object 의 property value 로 가능하다
 * object 의 property 함수를 메소드(method) 라 부른다.
 * object 안에서 this 는 '자기자신객체', 즉, 해당 object 가 참조(혹은 바인딩) 된 객체를 말한다
 */
console.log('-'.repeat(20));
console.log('[object method 와 this]');

obj3 = {
    firstName: "John",
    lastName: "Doe",
    id: 5566,

    fullName: function(){
        // return "Hello";
        return `${this.id}] ${this.firstName} ${this.lastName}`;
    },
}

console.log(obj3.fullName());

/**
 *  this 의 정체!
 *  JS code 를 소유한(own) object다!  즉 this 는 '특정 object' 를 '참조' 한다.
 * '어떤 object 를 참조하나?' → this 가 사용(호출) 되는 시점마다 '다르다'.
 *  (JS 의 this 가 다른 언어의 this에 비해 직관적으로 이해하기 어려운면이 있습니다)
 *
 *  가령
 * - 'object method' 내의 this 는 함수를 소유한(own) object 참조
 * - function 내의 this 는 global object 참조
 * - strict mode 에서 function 내의 this 는 undefined
 * - this 단독인 경우 global object 참조
 * - event 에선 this 는 event 가 발생한 element 객체
 * - '생성자(constructor) 안'에서의 this 는 그 자체가 값을 갖고 있진 않다.
 *    단지, 생성된 새로운 object에서 치환된다.
 *    즉 new 로 생성된 새로운 object 가 바로 this 가 된다.
 * - call(), apply(), bind() 와 같은 메소드에선 this 는 어떠한 object 를 참조하게 할수 있다.
 *
 * this 는 변수가 아니다!! 키워드다!!  따라서 this 의 값을 수정할수 없다
 */

let x = {
    name: "kim",
    age: 34,
    height: 172.3,
    score: [94, 35, 79],

    getTotal: function() {
        return this.score[0] + this.score[1] + this.score[2];
    },

    getAvg: function() {
        return this.getTotal() / this.score.length;
    },
}

console.log(x.score[1])
console.log(x.getTotal());
console.log(x.getAvg());