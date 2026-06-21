```python
access_token = auth.create_access_token(data={"sub": user.username})

```

JWT(Json Web Token)의 페이로드(Payload)에 들어가는 `'sub'`는 Subject(주제/대상)의 약자로, "이 토큰이 인증하고 있는 주체가 누구인가?"를 나타내는 표준 클레임(Claim) 이름입니다.

쉽게 말해, 토큰의 주인(유저)을 식별할 수 있는 고유한 ID나 ID 역할을 하는 문자열(예: username, email 등)을 담는 공간입니다.

JWT 명세(RFC 7519)에서는 토큰의 크기를 줄이기 위해 자주 사용되는 필수 데이터의 이름을 3글자 형태의 약어로 정의해 두었는데, 그중 하나가 바로 `sub`입니다.

---

### 💡 JWT 표준 클레임 종류 (약어 의미)

`sub` 외에도 JWT 생성 시 관례적으로 사용하는 대표적인 3글자 예약어들이 있습니다.

| 클레임 명 | 전체 이름 (Full Name) | 의미 | 우리 프로젝트에서의 예시 |
| --- | --- | --- | --- |
| **`sub`** | **Subject** | **토큰의 주인 (식별자)** | `"user1"` (username) |
| `exp` | Expiration Time | 토큰 만료 시간 (유닉스 타임스탬프) | `1781881200` |
| `iat` | Issued At | 토큰이 발급된 시간 | `1781879400` |
| `iss` | Issuer | 토큰 발급자 (서버 식별 명칭) | `"my-auth-server"` (선택 사항) |

---

### 🔍 우리 프로젝트 코드에서의 작동 방식

우리가 백엔드의 `auth.py`와 `controllers.py`에서 코드를 작성할 때 이 `sub`가 어떻게 쓰였는지 매핑해 보면 이해가 쉽습니다.

**1. 토큰을 만들 때 (`auth.py`)**

```python
# 로그인 성공 시 유저네임을 'sub'라는 키에 담아 JWT를 생성(인코딩)합니다.
access_token = auth.create_access_token(data={"sub": user.username})

```

이렇게 생성된 토큰을 디코딩해 보면 페이로드가 아래와 같은 JSON 형태를 띠게 됩니다.

```json
{
  "sub": "user1",
  "exp": 1781881200
}

```

**2. 토큰을 검증하고 유저를 찾을 때 (`controllers.py`)**
회원 전용 페이지로 요청이 들어오면 헤더의 토큰을 복호화(디코딩)하여 **`sub` 키에 들어있는 유저네임**을 쏙 빼옵니다.

```python
payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
username: str = payload.get("sub") # 결과: "user1"

# 꺼내온 sub(username) 정보로 DB를 조회해서 "아, user1이 요청했구나!" 하고 알아냅니다.
stmt = select(User).where(User.username == username)

```

### 📌 요약

`sub`는 JWT를 다루는 전 세계 개발자들이 "여기에 회원 식별 번호나 아이디를 넣자"고 약속한 표준 필드입니다. 꼭 `sub`가 아니라 `"username"`이나 `"user_id"` 같은 커스텀 키 이름을 써도 기술적으로는 작동하지만, 표준 규격을 준수하면 다른 라이브러리나 외부 서비스와 연동할 때 호환성이 극대화됩니다.