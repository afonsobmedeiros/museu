import os
import logging
import datetime

DEBUG = True

DATABASE = "MARIADB"

ROOT = os.path.dirname(os.path.abspath(__file__))

SECRET = "ADICIONE AQUI O SEU SEGREDO MAIS LONGO POSSIVEL"

JWT_SECRET = "ADICIONE AQUI O SEU SEGREDO MAIS LONGO POSSIVEL PARA JWT"

JWT_ALGORITHM = "HS256"

JWT_EXP_DELTA_SECONDS = 3600000  # 360 1 hora

logging.basicConfig(
    filename=os.path.join(
        ROOT,
        f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}",
    ),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)
