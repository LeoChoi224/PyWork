# 안전한 비밀키(secret key) 생성을 위해
# secrets 모듈 사용

import secrets

new_key = secrets.token_hex(32)
print('🔒 new_key =', new_key)
