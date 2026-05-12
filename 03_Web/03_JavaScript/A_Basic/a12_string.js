/* string 문자열 데이터
 *
 * string reference
 *  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String
 *  https://www.w3schools.com/jsref/jsref_obj_string.asp
 */
let str, str1, str2, str3;

/*******************************
 * 문자열 생성 
 * 
 * 방법1. 문자열 리터럴.  "~" 혹은 '~' 으로 생성
 * 방법2. new String() 으로 정의 (비추)
 */
console.log("[문자열 생성]");
// .length
console.log("length: 문자개수");
str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
console.log(str.length);
str = "가나다라"
console.log(str.length);  // 4


/******************************************
 * 문자열 인덱싱
 */
 console.log('-'.repeat(20));
 console.log('[문자열인덱싱]');
 str = "Hello World";
console.log(str[0]);
console.log(str[100]);

// 문자열은 immutabnle (불변) 객체
str[0] = 'Y';  // 에러도 발생하진 않는다.
console.log(str);

/******************************************
 * String 의 메소드들
 * 기본적으로 string 은 immutable 하기 때문에
 * string 메소드들은 원본을 변화시키기 않는다
 * 
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String#%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4_%EB%A9%94%EC%84%9C%EB%93%9C
 * 
 *  immutable : 데이터를 변경할수 없는 특성
 *  mutable : 데이터를 변경할수 있는 특성
 * 
 */
	
/******************************************
 *  문자열 안에서 문자열 찾기
 *  indexOf(), lastIndexOf(), search()
 *    찾은 위치 인덱스 리턴, 못찾으면 -1 리턴
 * 
 *  includes() : 찾으면 true 리턴
 *  startsWith(searchValue, start) : 주어진 문자열로 시작하면 true 리턴
 *  endsWith(searchValue, length): 주어진 문자열로 끝나면 true 리턴
 */
console.log('-'.repeat(20));
console.log("[문자열 검색 indexOf(), lastIndexOf(), search(), includes()]");
str = "Please locate where 'locate' occurs!";

console.log(str.indexOf("locate"));
console.log(str.lastIndexOf("locate"));
console.log(str.indexOf("김정준")); // -1

console.log(str.indexOf("locate", 15));  // 15부터 검색

console.log(str.search("locate"));  // 7
// search() vs indexOf() : 둘은 다르다!
// 	search() : 두번째 매개변수 없다, regexp 사용가능
// 	indexOf() : regexp 사용 불가

console.log(str);
console.log(str.includes("locate"));  // true
console.log(str.includes("abc"));  // false



/***********************************************
 *  문자열 추출
 *  slice(start, end) : start 부터 'end직전'까지 문자열 추출
 *  substring(start, end)
 *  substr(start, length) : start 부터 length 개의 문자 추출
 */
console.log('-'.repeat(20));
console.log("[문자열 추출 slice(), substring(), substr()]");
str = "Apple, Banana, Kiwi";

console.log(str.slice(7, 13));
console.log(str.slice(7));
console.log(str.slice(-12, -6));  // 음수인덱스 지원


/*******************************
 * 문자열 치환
 *  replace() : 치환한 결과 문자열 리턴, 정규표현식 사용 가능
 *  replace(..., func)
 *  기본적으로 첫번째 '매칭된 문자열 만 치환
 */
console.log('-'.repeat(20));
console.log("[문자열 치환 replace()]");
str = "Please visit Japan!";

console.log(str.replace("Japan", "Korean"));
console.log(str.replace("JAPAN", "Korean"));
console.log(str.replace(/JAPAN/i, "Korean"));  // 정규표현식 대소문자 구분없이 치환.


/*********************************
 * 대소문자 전환
 *  toUpperCase(), toLowerCase() 
 */
console.log('-'.repeat(20));
console.log("[대소문자 전환 toUpperCase(), toLowerCase()]");
str = "Hello World!";
 
console.log(str);
console.log(str.toUpperCase());
console.log(str.toLowerCase());

/*********************************
 * 문자열 연결 
*  concat(...strings)
 */
console.log('-'.repeat(20));
console.log("문자열 연결 concat()");
str1 = "Hello";
str2 = "World";
 
console.log(str1 + " " + str2);
console.log(str1.concat(" ", str2));


/**********************************
 * 좌우 공백 제거 
 *  trim()
 */
console.log('-'.repeat(20));
console.log("좌우 공백 제거 trim()");
str = "       Hello World!        ";

console.log(`[${str}]`);
console.log(`[${str.trim()}]`);

/************************************
 * 문자열 앞/뒤로 패딩문자 추가
 *  padStart(), padEnd()
 *  ECMA2017 에서 추가 https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/padStart
 */
// console.log('-'.repeat(20));
// console.log('[문자열 앞/뒤로 패딩문자 추가]');
// str = "5";

// TODO



/***********************
 * 문자 코드
 *  charAt(position)        # python ord()
 *  charCodeAt(position)    # python chr()
 *  Property access [ ] 
 */
// console.log('-'.repeat(20));
// console.log("[문자 코드 [ ], charAt(), charCodeAt()]");
// str = "HELLO WORLD";

// TODO

/************************
 * 문자열 대소 비교   <- 파이썬 과 동일 (코드값 비교)
 */

console.log("abcd" < "ABCD");

/*********************************
 * string ↔ array
 *   string -> array : split()  str의 메소드,  정규표현식(regexp) 사용 가능
 *   array -> string : join()   array 의 메소드
 */
console.log('-'.repeat(20));
console.log("[string ↔ array]");
str = "2022-11-23"; 

let arr = str.split("-"); // array 리턴
console.log(arr);

str = "Hello";
console.log(str.split());
console.log(str.split(""));

str = "    Hello  My   World      ";
console.log(str.split(" "));
console.log(str.trim().split(/\s+/));

arr = ["2026", "05", "12"];
console.log(arr.join("-"));

console.log(arr);
console.log(arr.reverse());

// 응용: 문자열 뒤집기.  
str = "hello";   // => "olleh"

console.log(str.trim().split("").reverse().join(""));
