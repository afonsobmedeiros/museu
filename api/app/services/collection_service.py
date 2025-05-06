from datetime import datetime
from config import logging
from app.repositories import collection_repository as cr


def create(exhibition_id: int, name: str, summary: str) -> int:
    try:
        return cr.create(name, summary, exhibition_id)
    except Exception as e:
        logging.error(e.message)


def update(collection_id: int, name: str, summary: str) -> int:
    try:
        return cr.update(collection_id, name, summary)
    except Exception as e:
        logging.error(e.message)