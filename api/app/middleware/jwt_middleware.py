from bottle import request, HTTPResponse
from app.utils.jwt_helper import decode_auth_token


def jwt_required(fn):
    def wrapper(*args, **kwargs):
        token = request.get_header("Authorization")
        if token and token.startswith("Bearer "):
            token = token[7:]
            user_id = decode_auth_token(token)
            if user_id:
                request.user_id = user_id
                return fn(*args, **kwargs)
        return HTTPResponse(status=401, body="Unauthorized")

    return wrapper
