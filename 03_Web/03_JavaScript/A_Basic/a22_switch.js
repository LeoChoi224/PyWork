/**********************************************
* switch - case 조건문
* 
* switch(조건값)
* {
* case 값1:
*	...
*	break;
* case 값2:
*	...
*	break;
*
* ...
* default:
*	...
*	break;
*}
* 	해당 조건값의 case문을 찾아서 거기서부터 break를 만날 때까지 실행을 함.
*  break를 만나게 되면 switch 문장을 종료.
*  해당하는 case가 없으면 default 문장을 실행함.
*  
*  	※ 모든 switch 조건문은 if - else if - else로 바꿀 수 있다. (할수 있어야 한다)
***************************************************/
let n = 2;

switch (n) {
    case 1:
        console.log('하나');
        console.log('ONE');
        break;
    case 2:
        console.log("둘");
        console.log("TWO");
        break;

    case 3:
        console.log("셋");
        console.log("THREE");
        break;

    default:
        console.log("몰라요~");


}


/*********************
 * 중첩 switch 문
***********************/
// console.log('-'.repeat(20))
