```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
```


이 코드는 FastAPI 보안 시스템의 핵심인 **"인증 가드(Authentication Guard)"** 역할을 하는 구간입니다.

코드에 담겨 있는 마법 같은 동작 원리를 2가지 핵심 포인트로 나누어 쉽게 설명해 드릴게요.

---

### 1. `oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")` 의 의미

이 한 줄은 "우리 서버는 이제부터 OAuth2 Bearer 토큰 인증 방식을 채택하겠다"라고 FastAPI 시스템에 선언하고 규칙을 정의하는 것입니다.

* **OAuth2PasswordBearer**: 클라이언트가 요청을 보낼 때, HTTP 헤더에 아래와 같이 토큰을 실어 보내야 한다는 규격을 강제하는 클래스입니다.
```text
Authorization: Bearer <JWT 토큰 문자열>

```


* **`tokenUrl="api/login"`**: 만약 사용자가 토큰 없이 회원 전용 페이지에 접근하거나 인증에 실패했을 때, **"토큰을 발급받으려면 여기(`api/login`) 주소로 가서 로그인해라"** 하고 가이드라인(URL 위치)을 지정해 두는 것입니다. (FastAPI가 자동으로 제공하는 Swagger UI 문서(`/docs`)에서 [Authorize] 버튼을 누를 때 이 주소로 로그인 창이 연동되기도 합니다.)

---

### 2. `token: str = Depends(oauth2_scheme)` 의 놀라운 자동화 동작

이 부분이 질문하신 코드의 핵심 메커니즘입니다. `Depends(oauth2_scheme)`가 실행되면 FastAPI는 백엔드 내부적으로 다음과 같은 과정을 **알아서, 자동으로** 처리합니다.

1. **헤더 검사 및 가로채기**: 클라이언트(프론트엔드 Axios)가 보낸 API 요청 헤더에서 `Authorization` 항목이 있는지 자동으로 뒤집니다.
2. **`Bearer` 접두사 제거**: 헤더에서 `Authorization: Bearer eyJhbGci...` 형태를 찾아내면, 앞의 `Bearer `라는 글자를 자동으로 떼어내고 순수한 **JWT 토큰 문자열만 쏙 추출**합니다.
3. **변수에 주입**: 그 추출한 순수 토큰 문자열을 `token: str` 변수에 값으로 넣어줍니다.
4. **자동 차단 에러 처리**: 만약 요청 헤더에 `Authorization` 자체가 없거나 포맷이 완전히 틀렸다면, 함수 내부 코드가 실행되기도 전에 FastAPI가 알아서 클라이언트에게 **`401 Unauthorized` (인증 유실)** 에러를 즉시 반환하며 요청을 차단해 버립니다.

---

### 🔄 전체적인 데이터 흐름 (요약)

회원이 로그인이 필요한 `/api/me` (회원 정보 조회)에 접근할 때 일어나는 순서입니다.

```text
[프론트엔드 요청] ➔ 헤더에 토큰 실어서 보냄 (Authorization: Bearer xxx)
       ↓
[get_current_user 실행]
       ↓
1. token: str = Depends(oauth2_scheme) 가 발동!
   -> 헤더에서 "xxx" 라는 순수 토큰 문자열만 자동으로 추출해서 'token' 변수에 저장.
       ↓
2. username = auth.verify_token(token)
   -> 념겨받은 "xxx" 토큰이 진짜인지, 유효기간은 안 지났는지 복호화 검증 (sub 유저네임 추출)
       ↓
3. stmt = select(User).where(User.username == username)
   -> 추출한 유저네임으로 실제 MySQL DB에 유저가 존재하는지 조회
       ↓
4. return user
   -> 무사히 통과하면 최종 인증된 User 객체를 엔드포인트 함수로 배달 완료!

```

즉, `Depends(oauth2_scheme)` 덕분에 개발자는 매번 헤더를 문자열로 쪼개고 파싱하는 노가다성 코드를 짤 필요 없이, **단 한 줄로 안전하게 유저의 토큰 문자열을 확보**할 수 있는 것입니다.