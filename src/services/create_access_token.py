import os
from jose import jwt
from datetime import datetime, timedelta, timezone

jwt_secret = os.environ.get('JWT_SECRET')
agl = "HS256"
access_token_expire_minutes = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_secret, algorithm=agl)
    return encoded_jwt