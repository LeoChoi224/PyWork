// 상속 : extends
// 이미 만들어진 클래스 활용
console.log("\n[extends]", "=".repeat(20));
{
  class Parent {
    name = "Lee";
    hello() {
      console.log("hello", this.name);
    }
  }

  class Child extends Parent {

  }

  const p = new Parent();
  const c = new Child();

  console.log(p);
  console.log(c);

  c.name = '김정준';

  console.log(p);
  console.log(c);

  c.hello;

}

// override
// 클래스의 상속 멤버 변수 및 함수 오버라이딩 추가
// 부모에서 구현된 함수나 변수를
// 자식에서 똑같이 구현하면 이를 '오버라이딩' 이라 함.
// 자식이 만든 함수가 부모에서 만들어져 있던 함수를 덮어쓰기 하는 셈
console.log("\n[override]", "=".repeat(20));
{
  class Parent {
    name = "Lee";
    hello() {
      console.log("hello", this.name);
    }
  }

  class Child extends Parent {
    age = 37;  // 추가 속성

    // 함수 오버라이딩
    hello() {
      console.log('🎃hello', this.name, this.age);
    }
  }

  const p = new Parent();
  const c = new Child();

  console.log(p);
  console.log(c);
}

// super
// 클래스의 상속 생성자 함수 변경
// 자식이 constructor 에 무언가 추가하고자 할때
console.log("\n[super]", "=".repeat(20));
{
  class Parent {
    name;
    constructor(name) {
      this.name = name;
    }

    hello() {
      console.log('hello', this.name)
    }
  }

  class Child extends Parent {
    age;

    constructor(name, age) {
      // super 없으면 에러!,  this 사용하기 전에 반드시 super() 명시해야 한다
      // this.name = name;
      super(name);   // 부모의 constructor(name)
      this.age = age;
    }

    hello() {
      console.log('hello', this.name, this.age)
    }
  }

  const p = new Parent('권용현');
  const c = new Child('신하석', 37);

  console.log(p);
  console.log(c);
  p.hello();
  c.hello();
}

// staic 상속
// static 도 정상적으로 상속된다
console.log("\n[staic 상속]", "=".repeat(20));
{
  // TODO
}

/*
    JS 의 상속 메커니즘

    부모    new       부모
    class  ─────────> Instance
      │                 │
      ↓                 ↓
    자식     new      자식
    class  ─────────> Inscance


*/

// 앞으로
// 보통.. Babel 을 사용하시거나
// class 를 사용할수 있는 런타임에서 작업하시게 될겁니다.
// class 는 꼭 익혀두셔야 합니다.

