// 얕은 복사  (JS 쪽에선 이를 깊은 복사라 하기도 한다.)

// 불변함수 (immutable function)
//  호출 원본을 변화시키지 않고 새로운 객체를 리턴하는 함수


// concat, filter, map, slice, spread 연산자

console.log("1. spread op.");
{
  const a = [1, 2, 3];
  const b = a;

  // TODO
}

console.log("\n2. concat 사용");
{
  const a = [1, 2, 3];
  // TODO
}

console.log("\n3. push() 를 사용하면?");
{
  const a = [1, 2, 3];
  // TODO
}

console.log("\n4. filter()");
{
  const a = [1, 2, 3];
  // TODO
}

/*
 ※ React 에서 불변함수 사용할때
    filter() 는 주로 '삭제' 할때 사용
    concat() 은 주로 '추가' 할때 사용
    spread 는 주로 '복사' + '추가' 할때 사용
    중간에 삽입하려면 slice 를 해야 한다.
 */

console.log("\n5. slice 잘라내기");
{
  const a = [1, 2, 3];
  // TODO
}

console.log("\n6. map()");
{
  const a = [1, 2, 3];
  // TODO
}

// React 불변 함수..
console.log("\n7 수정하기");
{
  // 우선 아래와 같은 데이터를 서버로부터 받아온 상태라 하자
  const users = [
    { id: 1, name: "John", phone: "111-1111" },
    { id: 2, name: "Susan", phone: "222-2222" },
    { id: 3, name: "Kelly", phone: "333-3333" },
  ];

  console.log(users);

  // TODO
}




