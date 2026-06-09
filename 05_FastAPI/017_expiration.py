# 🟦expiration 설정은 
# 서비스의 특성과 보안 요구 사항에 따라 다릅니다. 
# 다양한 시간 설정을 통해 토큰의 만료 시간을 제어할 수 있고, 
# 이는 파이썬의 datetime.timedelta를 사용하여 설정할 수 있습니다.

import jwt 

import secrets
SECRET_KEY = secrets.token_hex(32)

import datetime
utcnow = datetime.datetime.now(datetime.timezone.utc)

# JWT 만료 시간을 UTC 현재 시각에 1시간을 더해서 설정 (가장 많이 사용하는 설정)
expiration= utcnow + datetime.timedelta(hours=1) 

# 분 단위 만료 <- 로그인 세션에 적합하며, 금방 만료됩니다.
expiration = utcnow + datetime.timedelta(minutes=15) # <- 보통 금융권에서 사용

# 하루 만료 <- 주로 애플리케이션 내에서 꾸준한 사용이 이루어질 때 사용합니다.
expiration = utcnow + datetime. timedelta(days=1)

# 주 단위 만료 <- 장기간 로그인을 유지해야 할 때 사용합니다.
expiration = utcnow + datetime.timedelta (weeks=1)

# 연단위 만료
expiration = utcnow + datetime.timedelta(days=365)

# 영구 토큰
# 만료 시간(exp 클레임)을 설정하지 않으면 영구 토큰도 가능하지만, 
# 이 경우 토큰이 탈취되면 악의적인 사용자가 계속해서 해당 토큰을 사용할 수 있기 때문에 
# 실무에서는 사용하지 않습니다.

# 영구 토큰 예제 (하지만 권장하지 않음) 
def create_jwt_token(data: dict): 
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")

# 🟦실무에서는 다음과 같이 사용합니다.

# 🟡두 단계 만료: 
#   짧은 만료 시간을 가진 '액세스 토큰(access token)'과 
#   긴 만료 시간을 가진 '리프레시 토큰(refresh token)'을 함께 사용합니다.

# 🟡슬라이딩 세션: 사용자가 활동을 할 때마다 토큰의 만료 시간을 연장합니다.

# 🟡MFA(Multi-Factor Authentication): 
#   높은 보안이 필요할 때는 만료 시간을 더 짧게 설정하고 다단계 인증을 도입합니다.

# 🟡사용자 설정 만료: 
#   사용자가 선택할 수 있는 토큰 만료 시간을 제공하여 유연성을 높입니다.

# expiration 설정은 이와 같은 다양한 옵션과 실무 팁을 통해 최적화할 수 있습니다.