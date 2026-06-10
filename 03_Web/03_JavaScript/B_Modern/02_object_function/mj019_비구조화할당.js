// Destructuring Assigment (ES6 에서 등장) 문법
// '비구조화할당' 혹은 '구조분해할당' 이라고 번역이 됨.
// 객체변수.속성  <-- 좀더 편리하게 다룰수 있다.
// '비구조화할당 문법'
//   다른말로 '객체 구조 분해'

// 공식
// https://www.ecma-international.org/ecma-262/6.0/#sec-destructuring-assignment
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment

// 추가 참조
// https://velog.io/@public_danuel/destructuring-assignment
// 비구조화 할당, 잘 사용하면 코드 깔끔해진다

const ironMan = {
  name: "스타크",
  actor: "로다주",
  alias: "아이언맨"
};

const captainAmerica = {
  name: "스티브",
  actor: "크리스에반스",
  alias: "캡틴그놈"
};

{
  let actor = ironMan.actor
  let name = ironMan.name
  console.log(`배우: ${actor}, 이름: ${name}`)
}

//---------------------------------------------
// 객체의 구조분해
{
  console.log();
  let { actor, name } = ironMan;
  // 실제로 아래와 같이 ironMan 의 속성들이 분해(destructure)되어 대입(assign)된다.
  // let actor = ironMan.actor
  // let name = ironMan.name  
  console.log(`배우: ${actor}, 이름: ${name}`)


  // 해당 property 명으로 변수 선언 해야 한다.  그렇지 않으면 undefined 값이 들어온다.d
  let { ooo, qqq } = captainAmerica;
  // let ooo = captainAmerica.ooo;
  console.log(`ooo: ${ooo}, qqq: ${qqq}`);

}
{
  // object 정의한 순서와 무관

  // TODO

}
//----------------------------------------------------------------------
console.log('-'.repeat(20))

{
  let object = { a: 1, b: 2 };
  let { a, b } = object;
  console.log(a, b);

  // 함수 호출시에도 비구조화할당 발생
  console.log();
  let print = function ({ a, b }) {
    console.log(`🎃print(a=${a}, b=${b}) 호출`);
  };

  print(object);  // 호출시점에서 비구조화할당 
  print({ a: 10 });  // 분해할 값이 없는 b 는 undefined!

  // 비구조화 할당에서 default 값 가능.
  print = function ({ a, b = 2 }) {
    console.log(`🎃print(a=${a}, b=${b}) 호출`);
  };
  print({ a: 22 });

  let { c, d = 333 } = { c: 111, e: 222 };
  console.log(`c = ${c}, d = ${d}`);

}


//----------------------------------------------------------------------
console.log()

// 비구조화 할당시 이름 바꾸기
// 이번에는, 비구조화 할당을 하는 과정에서
// 선언 할 값의 이름을 바꾸는 방법을 알아보겠습니다.
{
  const animal = {
    name: "멍멍이",
    type: "개"
  };

  let nickname = animal.name;
  console.log(nickname); // 멍멍이

  let { name: nickname2 } = animal;
  // let nickname2 = animal.name;
  console.log(nickname2);

}

//--------------------------------------
// 배열 비구조화 할당
// 비구조화 할당은 객체에만 할 수 있는 것이 아닙니다.
// 배열에서도 할 수 있다!
console.log('-'.repeat(20))
{
  console.log('\n배열의 비구조화 할당')
  const array = [1, 2];

  let [one, two] = array;
  // let one = array[0];
  // let two = array[1];
  console.log(one, two);

  let [a, b, c] = array;
  console.log(a, b, c);   // 1 2 undefined

  [a, b, c = '희준정준'] = array;
  console.log(a, b, c);

  let [aaa, bbb] = [10, 30];
  console.log(`aaa = ${aaa}, bbb = ${bbb}`);
  [aaa, bbb] = [bbb, aaa];  // 변수값 swap
  console.log(`aaa = ${aaa}, bbb = ${bbb}`);
}


console.log('-'.repeat(40));
{
  //--------------------------
  // 깊은 값 비구조화 할당
  // 객체의 깊숙한 곳에 들어있는 값을 꺼내는 방법
  // Nested object and array destructuring
  //  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Nested_object_and_array_destructuring

  // console.log('\n깊은값 비구조화 할당');

  const deepObject = {
    state: {
      information: {
        name: "frogteam",
        languages: ["korean", "english", "chinese"]
      }
    },
    value: 5
  };

  
  // name, languages, value 들을 분해하고 싶다면?

  // 방법1: 비구조화할당 구문을 '두번' 사용
  const { name, languages } = deepObject.state.information;
  const { value } = deepObject;
  console.log(name, languages, value);

  // 방법2: object shorthand + destructuring assignment
  const extraced = {
    name,
    languages,
    value,
  };
  console.log(extraced);

  {
    const {
      // state,
      // state: {information},  // 이는 state 변수를 선언하게 아니라, information 변수 선언하여 구조분해
      state: {
        information: {name, languages},
      },
      value,
    } = deepObject;

    // console.log(state);
    // console.log(information);
    console.log(name, languages, value);
  }

  {
    // deepObject 로 부터 구조분해 하여 아래 object 만들기
    // {firstLang: "korean", secondLang: "english", thirdLang: "chinese"}


    // const [firstLang, secondLang, thirdLang] = deepObject.state.information.languages;
    // console.log({firstLang, secondLang, thirdLang});

    const {
      state: {information: {languages: [firstLang, secondLang, thirdLang]}}
    } = deepObject;

    console.log({firstLang, secondLang, thirdLang});

    // fistLang = deepObject.state.information.languages[0];
    // secondLang = deepObject.state.information.languages[1];
    // thirdLang = deepObject.state.information.languages[2];
  }
}







