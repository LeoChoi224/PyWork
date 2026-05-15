/**
 * Axios 란
 *    Promise API를 활용하는 HTTP '비동기' 통신 라이브러리.
 *
 * 특징]
 *    ▶운영 환경에 관계없이 동일한 코드로 작성가능
 *      내부적으론
 *          '브라우저' 환경에선  XMLHttpRequest 객체 사용
 *          'Node.js' 환경에선 HTTP API를 사용
 *    ▶ response 를 자동으로 JSON 으로 만든다
 *
 * 공식] https://axios-http.com/
 *       https://axios-http.com/kr/  (한국어)
 *
 * 설치]
 *     ① Node.js 에서 설치
 *          > npm install axios
 *            혹은
 *          > yarn add axios
 *
 *     ② CDN (들)
 *         <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
 *            혹은
 *         <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
 */

/**
 *  [request '요청'하기]
 *
 *  axios(config)
 *
 *  config object :   https://axios-http.com/docs/req_config
 *
 *     method:   <- 'get', 'post', 'put', 'delete', ....
 *     url:
 *     baseURL:   (옵션)
 *     headers:
 *     params:    <- URL parameter
 *     data:      <- request body 에 담겨 전송할 데이터. POST, PUT, DELETE, PATCH method 에서 사용
 *     responseType:  <- 서버로부터 받을 데이터 명시. 디폴트는 'json'
 *     timeout:   <-  서버로의 요청 timeout 시간. 디폴트는 '0' (no limit)
 */

/**
 *  편의를 위한 request method 들 제공
 *
 *    axios.request(config)
 *    axios.get(url[, config])
 *    axios.delete(url[, config])
 *    axios.head(url[, config])
 *    axios.options(url[, config])
 *    axios.post(url[, data[, config]])
 *    axios.put(url[, data[, config]])
 *    axios.patch(url[, data[, config]])
 *    axios.postForm(url[, data[, config]])
 *    axios.putForm(url[, data[, config]])
 *    axios.patchForm(url[, data[, config]])
 *
 */

/**
 * resposne 구조 : https://axios-http.com/docs/res_schema
 *   응답 형태는 json 형태
 *
 *    data:    <- 서버로부터의 응답
 *    status:     <- http status code. ex) 200
 *    statusText:   <--  http status message  ex) 'OK'
 *    headers:
 *    config:
 *    request:
 */

/*
  Ex)
  axios(config)
    .then(function (response) {
      // 성공 핸들링
      console.log(response);
    })
    .catch(function (error) {
      // 에러 핸들링
      console.log(error);
    })
    .finally(function () {
      // 항상 실행되는 영역
    });

  Ex)
  axios.get(url)
    .then(function (response) {
      // 성공 핸들링
      console.log(response);
    })
    .catch(function (error) {
      // 에러 핸들링
      console.log(error);
    })
    .finally(function () {
      // 항상 실행되는 영역
    });
*/

// TODO