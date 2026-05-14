/*
 * while 순환문
 * 
 * [구문]
 *  while(조건식) {
 *        ...
 *  }
 * 
 * 조건식이 '참' 인 동안 while 블럭 반복
 * 
 */

let count = 1, total = 0;
while(count <= 10){
    console.log(`count = ${count}`);
    total += count;
    count++;
}

console.log(`total = ${total}`);

