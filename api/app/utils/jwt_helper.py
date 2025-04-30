import jwt
import datetime
from config import JWT_SECRET, JWT_ALGORITHM, JWT_EXP_DELTA_SECONDS


def encode_auth_token(user_id):
    payload = {
        "exp": datetime.datetime.now(datetime.UTC)
        + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        "sub": str(user_id),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
