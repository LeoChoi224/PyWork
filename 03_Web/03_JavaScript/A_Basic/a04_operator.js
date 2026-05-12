/*
 * 연산자 관련 일반사항
 * 
 * 연산 Operation
 * 연산자  Operator
 * 피연산자 Operand
 * 
 * ■ 피연산자의 개수에 따라
 * 이항연산자(binary operator) : 피연산자가 2개인 연산자 
 * 단항연산자(unary operator) : 피연산자가 1개인 연산자
 * 삼항연산자(ternary operator) : 피연산자가 3개인 연산자
 * 
 * ■ 피연산자의 타입에 따라 수행하는 연산이 달라지는 연산자들도 있다  (ex: +  )
 * 
 * ■ 모든 연산은 연산의 결과값을 리턴한다 (어떠한 '값'인지?, 어떤 '타입'인지? 주목)
 * 
 * ■ 관례적으로 이항연산자는 피연산자와 연산자 간에 한칸씩(space) 띄어주는게 좋다
 *   단항연산자는 피연산자와 연산자를 붙여주는게 일반.
 */

let num1, num2, num3, num4, num5, num6, num7, num8, num9, num10

/* 
    대입 연산자 assignment operator : =
    등호(=) 오른쪽의 값을 왼쪽에 대입(저장)

    산술 연산자 arithmetic operator : 
    +, -, *, / : 사칙연산
    % : 나머지 연산자 (remainder) 
    ** : 제곱연산자 (exponential)  ES2016
 */
console.log('[대입연산자, 산술연산자]');

num1 = 7;
num2 = 3;

console.log(num1 / num2);
console.log(4 / 2);
console.log(4 / 2.0);


/* 
    복합대입연산자
    +=, -=, *=, /=, %=, **=      

 */
// console.log('-'.repeat(20))
// console.log('[복합 대입연산자]')

// TODO


/* 
    부호연산자(+, -) sign operator
        +: 부호 연산자(수의 부호(양,음)가 바뀌지 않음)
        -: 부호 연산자(수의 부호(양,음)가 바뀜)  
*/
// console.log('-'.repeat(20))
// console.log('[부호연산자]')

// TODO

/* 
    증감연산자 increment/decrement operator : 
    ++변수: 변수의 값을 1 증가시켜서 저장
    --변수: 변수의 값을 1 감소시켜서 저장

    증감연산자: prefix(접두사), postfix(접미사)
    접두사(prefix)인 경우에는, 증감(++, --)이 먼저 된 후 다른 연산자가 동작
    접미사(postfix)인 경우에는, 다른 연산자 먼저 실행된 후 증감(++, --)가 동작

 */
console.log('-'.repeat(20))
console.log('[증감연산자]')

num1 = 100;
console.log('num1 =', num1);

num1 += 1;
console.log('num1 =', num1);

num1++;
console.log('num1 =', num1);

++num1;
console.log('num1 =', num1);

num4 = 100;
num5 = ++num4; // prefix: 다른 연산자보다 먼저 ++ 연산 실행
console.log('num4 =', num4, 'num5 =', num5);

num4 = 100;
num5 = num4++; // postfix: 다른 연사자 실행한 다음에 ++연산 실행
console.log('num4 =', num4, 'num5 =', num5);

num4 = 100;
num5 = num4;
num4++;
console.log('num4 =', num4, 'num5 =', num5);

/* 
    관계(비교) 연산자   Equality and Relational Operators
    비교 연산의 결과를 참(true) 또는 거짓(false)으로 리턴하는 연산자
    A < B: A는 B보다 작다
    A > B: A는 B보다 크다
    A >= B: A는 B보다 크거나 같다 
    A <= B: A는 B보다 작거나 같다
    A == B: A와 B가 같다.  ('값' 만 비교)
    A != B: A와 B는 다르다. ('값' 만 비교)
    A === B : A 와 B 는 '값' 과 '타입' 이 같다
    A !== B : A 와 B 는 '값' 혹은 '타입' 이 다르다
 */
console.log('-'.repeat(20))
console.log('[비교연산자]')

console.log(10 == 10);  // true
console.log(10 == "10"); // true 값 만 비교
console.log(10 === "10"); // false '타입' 과 '값' 비교


/* 논리 연산자 (logical operator) :  &&, ||, !
 *	A && B: (AND 연산) A와 B가 모두 참일 때만 결과가 true, 나머지는 결과가 false
 *	A || B: (OR 연산) A나 B 둘 중 하나가 참이면 결과가 true, 둘 다 거짓이면 결과가 false
 *	!A	: (NOT 연산) A가 참이면 결과가 false, 거짓이면 결과가 true
 */
console.log('-'.repeat(20))
console.log('[논리 연산자]')

console.log(10 > 0 && 10 < 100); // true
console.log(10 > 0 && 10 < 10); // false
console.log(10 > 0 || 10 < 10); // true
console.log(!(10 > 0) || 10 < 10); // false

/*
    비트연산자 (bitwise operator)
    
    JS의 비트연산자는 32bit number 에 대해 연산한다
    비트연산자의 피연산자는 32bit number 로 변환된뒤 비트연산수행하고
    그 결과는 다시 JS number 타입으로 리턴된다.

    a & b: (and) a,b가 모두 1 이면 결과도 1, 그 외에는 0
    a | b: (or) a가 1이거나 또는 b가 1이면 결과는 1, a,b 모두 0일 때만 0
    a ^ b: (xor) a와 b 둘 중 하나만 1이 있는 경우는 1, 그 외에는 0
              결국 둘이 같으면 0, 다르면 1
     ~a  : (not) a가 1이면 0, a가 0이면 1로 바꿔줌

    a >> n : right shift   비트를 오른쪽으로 n 비트씩 이동
    a << n : left shift   비트를 왼쪽으로 n 비트씩 이동
*/
// console.log('-'.repeat(20))
// console.log('[비트 연산자]')


console.log('\n[삼항연산자]')

// (조건식) ? 참일때 값 : 거짓일때 값

// 파이썬 =>  참일때값  if (조건식) else 거짓일때 값

num1 = 34;
num2 = 56;

diff = (num1 > num2) ? (num1 - num2) : (num2 - num1);
console.log(diff);