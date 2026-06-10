// ES6 에선 object 에서 메소드 정의를 위한 단축구문(shorthand syntax)이 도입
//  
//  ex ) foo : function() {}  
//         => foo() {}   단축구문
// 
//  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Method_definitions

const dog = {
    name: "멍멍이",
    sound: "멍멍!",

    // 방법1 : 이름있는 함수
    say1 : function aaa(){
        console.log(`say1: ${this.sound}`)
    },

    // 방법2 : 이름없는(anonymous) 함수
    say2 : function(){
        console.log(`say2: ${this.sound}`)
    },

    // 방법3 : ES6 에서 도입한 메소드 정의 단축구문(shorthand syntax)
    say3() {
        console.log(`say3: ${this.sound}`);
    },

    // 화살표 함수는 this 가 바인딩 되지 않는다!
    say4: () => {
        console.log(`say4:`, this);  // {}
        console.log(`say4: ${this.sound}`);
    },
    // 이유
    // function 키워드로 만든 함수에서의 
    // this 라 하는 context 를 생성하여 
    // this 가 자기가 속해있는, object 를 가리키는데..

    // 화살표 함수의 경우
    // this context 를 생성하지 않습니다.
    // 따라서 this를 자기가 속해 있는 곳으로 연결하지 않습니다.
    // 화살표 함수는 this 가 뭔지 모릅니다!
    
}

dog.say1()
dog.say2()
dog.say3()
dog.say4();

console.log('-'.repeat(20));

// this 가 연결된다는 의미에 대해 알아보자
const cat = {
    name: "야옹이",
    sound: "야용~",
};

cat.say1 = dog.say1;

dog.say1(); // 호출시점에서 say1() 의 this 는 dog 에 연결 (say1() 의 owner 가 dog )
cat.say1(); // 호출시점에서 say1() 의 this 는 cat 에 연결

const catSay = cat.say1;
catSay();  // this 에 연결된게 없다.
          // 사실 이때 say1() 내의 this 는 global object 가 된다.




