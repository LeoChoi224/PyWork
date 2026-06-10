// 얕은 복사  (JS 쪽에선 이를 깊은 복사라 하기도 한다.)

// 불변함수 (immutable function)
//  호출 원본을 변화시키지 않고 새로운 객체를 리턴하는 함수


// concat, filter, map, slice, spread 연산자

console.log("1. spread op.");
{
  const a = [1, 2, 3];
  const b = a;

  console.log(a == b);  // true

  const c = [...a];  // 얕은 복사 발생 (새로운 객체 생성)
  console.log('a', a);
  console.log('c', c);
  console.log(a == c);  // false

  const a2 = { id: 1, name: "김정준" };
  const b2 = a2;
  console.log(a2 == b2);  // true 

  const b3 = { ...a2 };  // 새로운 객체 생성
  console.log(a2 == b3);  // false
  console.log('b3', b3);

  b2.name = '장희준';
  console.log('a2', a2);
  console.log('b2', b2);

  // 얕은 복사 할때 id값은 그대로인데 name 값만 변경
  const b4 = { ...b3, name: '문태현' };  // name값 변경된 새로운 객체 생성
  console.log('b3', b3);
  console.log('b4', b4);

  // 변경하고픈 데이터가 다음과 같이 주어진다면
  const data = { name: "박지원" };
  const b5 = { ...a2, ...data };
  console.log('b5', b5);

}

console.log("\n2. concat 사용");
{
  const a = [1, 2, 3];
  const b = a.concat(4);  // concat 은 불변함수. 원본 a 는 변경시키지 않고 새로운 객체 생성하여 리턴
  console.log('a', a);
  console.log('b', b);

}

console.log("\n3. push() 를 사용하면?");
{
  const a = [1, 2, 3];
  const b = a;
  b.push(4);  // push 는 불변함수 아니다. 원본 b 의 내용을 변경시킨다.
  console.log('a', a);
  console.log('b', b);
}

console.log("\n4. filter()");
{
  const a = [1, 2, 3];
  const b = a.filter(x => x !== 1)
  console.log('a', a);
  console.log('b', b);
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
  const b = a.slice(0, 2)   // slice() 는 불변함수
  console.log('a', a);
  console.log('b', b); 

    // 중간에 삽입하기
    //  [1, 2, 3] =>  [1, 2, 4, 3]
  let c = [...a.slice(0, 2), 4, ...a.slice(2)];
  console.log('c', c);
}

console.log("\n6. map()");
{
  const a = [1, 2, 3];
  const b = a.map(x => x * 2);   // 불변함수 map()
  console.log('a', a);
  console.log('b', b);  
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

  // 이후 아래와 같은 변경사항이 서버로부터 전달되어옴
  let updateUserDto = {id: 2, name: '홍길동'};
  
  // 이렇게 하면 되지 않나?
  users[1].name = updateUserDto.name;
  console.log(users);  // 바뀌긴 하는데...


  // map + spread 사용
  const newUsers = users.map(user => user.id === updateUserDto.id ? {...user, ...updateUserDto} : user);
  console.log(newUsers);
  console.log(users == newUsers);  // false
  console.log(users[0] == newUsers[0]);  // true
  console.log(users[1] == newUsers[1]);  // false
  console.log(users[2] == newUsers[2]);  // true

}

//────────────────────────────────────────────────────────────────────
