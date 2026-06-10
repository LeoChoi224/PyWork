const axios = require("axios");

/**
 * 자주 사용하게 되는 세팅의 axios 인스턴스를 미리 만들어 사용하면 편리하다
 * https://axios-http.com/kr/docs/instance
 *  axios.create({사용자 지정 config})
 */
// 

const baseURL = 'https://httpbin.org/';

// TODO

// then() 에 전달할 함수 준비.  (결과 확인용)
const printData = (response) => {
    const {data} = response;
    console.log(data);
}

(async function(){

    console.log('🧡'.repeat(10));
    // TODO

    console.log('🧡'.repeat(10));    
    // TODO

    console.log('🧡'.repeat(10));
    // TODO

    console.log('🧡'.repeat(10));
    // TODO

    console.log('💚'.repeat(10));
    // TODO
    console.log('💚'.repeat(10));
    // TODO

    
    

})();


/**
 * 혹은
 * axios 의 default config 로 설정할수도 있다.
 * https://axios-http.com/docs/config_defaults
 */

// TODO