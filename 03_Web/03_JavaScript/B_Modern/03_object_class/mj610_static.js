//---------------------------------------------
// static 변수, 함수
// 클래스의 변수와 함수에 적용되는 키워드
//  new 없이도 사용가능하다.  -->  클래스이름.이름
console.log("\n[static]\n");

class Alpha {
  username = '김정준';
  static age = 37;
  static hello() {
    console.log(this.age);
  }
}

console.log(Alpha)  // [class Alpha]
a1 = new Alpha(); a1.age = 67;
a2 = new Alpha(); a2.username = '문태현';
console.log(a1, a2);
console.log(Alpha.age);
// a1.hello();  // a1.hello is not a function
// a2.hello();
Alpha.hello();

class Beta {
  age = 37;  // non-staic
  static hello() {
    console.log(this.age);  // static 에서 non-static 접근 가능?
  }
}

console.log(Beta);
console.log(Beta.age);  // undefined
console.log(new Beta().age);  // 37
Beta.hello();  // undefined

console.log(Beta.name);  // Beta


