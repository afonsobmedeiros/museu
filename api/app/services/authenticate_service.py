from hashlib import md5
from passlib.hash import pbkdf2_sha512 as hsh
from config import SECRET
from app.utils.jwt_helper import encode_auth_token
from app.repositories import curator_repository as cr


def authenticate(email: str, password: str) -> dict:
    """Make authentication and generate JWT Token.

    Args:
        email (str): Curator E-mail.
        password (str): Curator password.

    Returns:
        dict: Dictionaty with JWT Token.
    """
    curator = cr.get_curator_by_email(email)
    if curator and verify(password, curator['password']):
        token = encode_auth_token(curator['id'])
        return {'token': token}
    return None


def gen_hash(password: str) -> str:
    """Generate hash for curator password.

    Args:
        password (str): Curator Password.

    Returns:
        str: hash curator password.
    """
    secret = md5(SECRET.encode()).hexdigest()
    _password = md5(password.encode()).hexdigest()
    return hsh.hash(secret+_password)


def verify(password: str, password_hash: str) -> bool:
    """Verify if password match with hash password.

    Args:
        password (str): Password for verification.
        password_hash (str): Saved hash curator password.

    Returns:
        bool: true if password match, false if not.
    """
    secret = md5(SECRET.encode()).hexdigest()
    _password = md5(password.encode()).hexdigest()
    salted = secret+_password
    return hsh.verify(salted, password_hash)
