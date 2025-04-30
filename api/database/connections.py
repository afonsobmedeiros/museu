from config import DATABASE
from .mysql_connection import get_mysql_connection

def get_connection():
    if DATABASE == "MARIADB" or DATABASE == "MYSQL":
        return get_mysql_connection()