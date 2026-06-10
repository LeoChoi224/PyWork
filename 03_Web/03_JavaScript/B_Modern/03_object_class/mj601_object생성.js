// 객체 object

// 함수 or 클래스 (틀)  --->  객체, 개체, object 생성
//                           생성된 객체를 (인스턴스)라고도 함

//-------------------------------------------------
// 생성자 함수로 객체 만들기
//     (틀)                  (인스턴스)
// function () {}  ----->   new 함수()

{
    function A(){};
    A();  // 함수 호출
    const a = new A();  // 객체 생성
    console.log(a, typeof a);
}

{
    function Beta(name, age){
        console.log(`Beta(name = ${name}, age = ${age})`);

        // 객체에 속성 추가.
        this.name = name;
        this.age = age;
    }

    const b1 = new Beta();  // 생성자 인자 없으면 name, age 에는 undefined 값
    const b2 = new Beta('Mark', 34);

    console.log('b1', b1);
    console.log('b2', b2);
}



