const axios = require("axios");

/**
 * 자주 사용하게 되는 세팅의 axios 인스턴스를 미리 만들어 사용하면 편리하다
 * https://axios-http.com/kr/docs/instance
 *  axios.create({사용자 지정 config})
 */
// 

const baseURL = 'https://httpbingo.org/';

const axios1 = axios.create({
    // baseURL: baseURL,
    baseURL,

    headers: {
        // 기본 header 값
        'Authorization': 'AUTH_TOKEN',

        // 각 request method 별로 기본 header 값 설정 가능.
        get: {
            'x-key': 'abcdef',
        },
        post: {
            'Content-Type': "application/json;charset=utf-8",
            'Secret': "HELLO SECRET",
        },
        put: {
            'Content-Type': "text/plain;charset=utf-8",
        },
    },

})


// then() 에 전달할 함수 준비.  (결과 확인용)
const printData = (response) => {
    const { data } = response;
    console.log(data);
}

(async function () {

    console.log('🧡'.repeat(10));
    await axios1.get('get')   // 'https://httpbingo.org/' + 'get
        .then(printData);

    console.log('🧡'.repeat(10));
    await axios1.get('get', {
        params: { name: "김정준", age: 23 },
    }).then(printData);

    console.log('🧡'.repeat(10));
    await axios1.post('post', {  // post() 함수의 두번째 매개변수는 request body data
        name: "하석이",
        age: 8,
    }).then(printData)

    console.log('🧡'.repeat(10));
    await axios1.put('put', "집에 가고싶다").then(printData);

    console.log('💚'.repeat(10));
    await axios2.get('get').then(printData);

    console.log('💚'.repeat(10));
    await axios2.post('post', 'name=John&age=20&age=44').then(printData);
})();


/**
 * 혹은
 * axios 의 default config 로 설정할수도 있다.
 * https://axios-http.com/docs/config_defaults
 */

const axios2 = axios.create();

axios2.defaults.baseURL = baseURL;
axios2.defaults.headers.common['Authorization'] = 'AUTH_TOKEN';  // common 은 공통 헤더
axios2.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// 특정 환경변수 값
console.log(process.env.PATH);

// 환경변수 활용
// axios2.defaults.baseURL = process.env.REACT_APP_Server;
// 여러 모듈이 있을때ㅣ
