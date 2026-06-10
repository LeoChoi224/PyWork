/*
클래스 class

클래스라는 기능은 C++, Java, C#, PHP 등의 
다른 프로그래밍 언어에는 있는 기능인데 

자바스크립트에는 없었기 때문에 
예전 자바스크립트 (ES5) 에서는 
클래스 문법이 따로 없었기 때문에 위에서 작성한 코드처럼 
객체 생성자 함수를 사용하여 비슷한 작업을 구현해왔습니다.

ES6 에서부터는 class 라는 문법이 추가되었는데요, 
우리가 객체 생성자로 구현했던 코드를 조금 더 명확하고, 
깔끔하게 구현 할 수 있게 해줍니다. 

추가적으로, 상속도 훨씬 쉽게 해줄 수 있습니다.

  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes

  
  clsss 가 .. 새로운 상속등의 모델(새로운 언어 기능?)을 제공하는건 아님!
  기존의 프로토타입 기반의 방식을 좀더 '명료하게' 사용할 수 있도록 하는
  일종의 '도우미' 정도라고 보면 된다.

*/

//------------------------------------------------------------
console.log()
// class를 만드는 2가지 방식
{
  // 1. 선언적 방식

  class Alpha {}
  console.log(new Alpha());

  // 2. class 표현식을 변수에 할당
  const Beta = class { };
  console.log(new Beta());

}

// constructor
// 최초 초깃값을 객체 안에 집어넣기
console.log('\n생성자');
{
  class Alpha {}
  console.log(new Alpha());

  class Beta {
    constructor() {
      console.log('Beata() 생성자 호출');
    }
  }
  console.log(new Beta());
}


// 프로퍼티 property 
console.log()
{
  // 방법1: constructor 에서 property 명시
  class Alpha {
    constructor(name, age){
      this.name = name;
      this.age = age;
    }
  }

  let a1 = new Alpha('김정준', 27);
  let a2 = new Alpha('문태현');
  let a3 = new Alpha();

  console.log(a1);
  console.log(a2);
  console.log(a3);



  // 방법2: class field 를 직접 기술
  class Beta {
    name;   // <-- this.name   초깃값 없으면 undefined 로 초기화
    age;   // <-- this.age
  }

  console.log(new Beta())

  class Gamma {
    name = '양정운';  // 필드 기본값
    age = 23;
  }
  console.log(new Gamma());

  class Theta {
    name;
    age;

    constructor(name = '이민재', age = 26) {
      this.name = name;
      this.age = age;
    }
  }

  console.log(new Theta());
  console.log(new Theta('박영진', 39));
}

