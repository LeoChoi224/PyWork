/* 대표적인 정규 표현식 
 *  구글링 하면 대표적인 정규표현식들이 많이 구할수 있습니다.
 *  각 정규표현식들을 작성해보고
 *	매칭되는 문자열과 그렇지 않은 것들을 출력해봅시다.   
 */

// 도우미 메소드
function regExpTest(regex, input){
    console.log("[정규표현식 매칭 테스트]-----------------");
    console.log("정규표현식:", regex);
    console.log("입력문자열:", input);

    if(regex.test(input)){
        console.log("   ⊙매칭⊙");
    } else {
        console.log(" X매치 없슴X");
    }
    console.log();
}

function test(regex, arrInput){
    for(input of arrInput) regExpTest(regex, input);
}

//--------------------------------------------------
let title, regex, arrInput;
console.log('[많이 쓰는 정규표현식]')

{
    //─────────────────────────────────────────
    title = "URL";
    regex = /TODO/;
    arrInput = [
        

    ];
    console.log(title);
    test(regex, arrInput);


    //─────────────────────────────────────────
    title = "email";
    regex = /TODO/;
    arrInput = [
        

    ];
    console.log(title);
    test(regex, arrInput);
    
    //─────────────────────────────────────────
    title = "주민등록번호";
    regex = /TODO/;
    arrInput = [
        

    ];
    console.log(title);
    test(regex, arrInput);

    //─────────────────────────────────────────
    title = "날짜 YYYY-MM-DD";
    regex = /TODO/;
    arrInput = [
        

    ];
    console.log(title);
    test(regex, arrInput);

    //─────────────────────────────────────────
    title = "자연수";
    regex = /TODO/;
    arrInput = [
        

    ];
    console.log(title);
    test(regex, arrInput);

    //─────────────────────────────────────────
    title = "정수";
    regex = /TODO/;
    arrInput = [
        

    ];
    console.log(title);
    test(regex, arrInput);

    //─────────────────────────────────────────
    title = "소수";
    regex = /TODO/;
    arrInput = [
        

    ];
    console.log(title);
    test(regex, arrInput);

    //─────────────────────────────────────────
    title = "소수점 둘째자리까지";
    regex = /TODO/;
    arrInput = [
        

    ];
    console.log(title);
    test(regex, arrInput);

    //─────────────────────────────────────────
    title = "1000 단위 콤마 자연수";
    regex = /TODO/;
    arrInput = [
        

    ];
    console.log(title);
    test(regex, arrInput);

}



console.log("\n[프로그램 종료]", '\n'.repeat(10));


