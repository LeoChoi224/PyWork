// 상속 : extends
// 이미 만들어진 클래스 활용

{
  class Parent {
    name = "Lee";
    hello() {
      console.log("hello", this.name);
    }
  }

  // TODO
}

// override
// 클래스의 상속 멤버 변수 및 함수 오버라이딩 추가
// 부모에서 구현된 함수나 변수를
// 자식에서 똑같이 구현하면 이를 '오버라이딩' 이라 함.
// 자식이 만든 함수가 부모에서 만들어져 있던 함수를 덮어쓰기 하는 셈
{
  class Parent {
    name = "Lee";
    hello() {
      console.log("hello", this.name);
    }
  }

  // TODO
}

// super
// 클래스의 상속 생성자 함수 변경
// 자식이 constructor 에 무언가 추가하고자 할때
//
{
  class Parent {
    // TODO
  }

  // TODO
}

// staic 상속
// static 도 정상적으로 상속된다
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




