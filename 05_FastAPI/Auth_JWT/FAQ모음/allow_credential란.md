`allow_credentials=True`는 CORS(Cross-Origin Resource Sharing) 설정에서 "서버와 클라이언트가 서로 주고받는 요청/응답에 쿠키(Cookie), 인증 헤더(Authorization Header), 또는 TLS 클라이언트 인증서 같은 보안 자격 증명(Credentials)을 포함하는 것을 허용하겠다"고 선언하는 설정입니다.

---

### 💡 왜 이 설정이 필요할까요?

브라우저에는 SOP(Same-Origin Policy, 동일 출처 정책)라는 기본 보안 가이드가 있습니다. 주소가 다른 프론트엔드(`http://localhost:5173`)와 백엔드(`http://localhost:8000`)가 통신할 때, 브라우저는 보안상의 이유로 요청에 담긴 민감한 인증 정보(쿠키나 Authorization 헤더 등)를 백엔드로 함부저 전달하지 않거나, 백엔드가 준 응답을 프론트엔드 자바스크립트가 읽지 못하게 차단합니다.

이때 백엔드에서 `allow_credentials=True`를 명시해 주어야만, 브라우저가 안심하고 "아, 이 백엔드 서버는 인증 정보를 주고받아도 안전하다고 허락했구나"라고 판단하여 차단을 해제합니다.

---

### ⚠️ `allow_credentials=True` 설정 시 반드시 주의할 점 (보안 규칙)

CORS 표준 규격상 `allow_credentials=True`를 사용할 때는 **보안을 위해 매우 엄격한 규칙**이 강제됩니다.

* **`allow_origins=["*"]`(와일드카드)를 절대 사용할 수 없습니다.**
인증 정보를 주고받는데 모든 도메인(`*`)을 허용하면 해킹(CSRF 공격 등)에 취약해지기 때문에, 브라우저 단에서 에러를 뿜으며 요청을 원천 차단합니다.
* 따라서 위 코드처럼 `allow_origins=["http://localhost:5173"]`와 같이 **신뢰할 수 있는 구체적인 프론트엔드 주소를 명확히 명시**해야만 정상적으로 작동합니다.

---

### 🔍 우리 프로젝트에서의 역할

현재 프로젝트에서는 JWT 토큰을 요청 헤더(`Authorization: Bearer <토큰>`)에 실어서 보내고 있습니다. Axios 인터셉터가 이 헤더를 붙여서 보낼 때, 백엔드의 `allow_credentials=True` 설정 덕분에 브라우저의 거부 반응 없이 백엔드 컨트롤러까지 안전하게 도달할 수 있는 것입니다.