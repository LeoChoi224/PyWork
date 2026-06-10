// getter & setter
// 일반적으로 클래스 '내부적으로만' 사용하는 변수명을
// _name 과 같이 언더바로 작명하는 경우 많음
// _ 언더바로 시작하는 변수명에 readonly 동작시킬수 있는 것이 있슴.
// 이런 용도의 멤버변수를 외부에서 접근할때 getter, setter를 통해 접근

{
  class Alpha {
    _name = 'no name';

    get name(){
      console.log('🟦Alpha: name getter 호출');
      return this._name + '😎😎';
    }

    set name(value){
      console.log('🟩Alpha: name setter 호출');
      this._name = value;
    }

  }

  const a = new Alpha();
  console.log(a);
  console.log(a.name);  // getter 는 '읽기 동작'할때 작동
  a.name = '김정준';    // setter 는 '쓰기 동작' 할때 작동
  console.log(a);
  console.log(a.name);
}

// readonly
{
  class Beta {
    _name = 'unknown';

    get name(){
      console.log('🟪Beta name getter 호출');
      return this._name;
    }

    // setter 는 없다.
  }

  const b = new Beta();
  console.log(b);
  console.log(b.name);

  b.age = 10;
  console.log(b);

  b.name = '최홍목';
  console.log(b);
}
