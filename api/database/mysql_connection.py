import os
import pymysql
from config import ROOT


def get_mysql_connection():
    return pymysql.connect(
        read_default_file=os.path.join(ROOT, 'my.cnf'),
        cursorclass=pymysql.cursors.DictCursor
    )