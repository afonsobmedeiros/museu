from config import logging
from datetime import datetime
from app.repositories import exhibition_repository as er


def create(
    curator_id: int, name: str, summary: str, start_at: str, finish_at: str
) -> int:
    try:
        return er.create(
            name,
            summary,
            datetime.fromisoformat(start_at),
            datetime.fromisoformat(finish_at),
            curator_id,
        )
    except Exception as e:
        logging.error(e.message)


def update(
    exhibition_id: int,
    name: str,
    summary: str,
    start_at: datetime,
    finish_at: datetime,
):
    try:
        return er.update(
            exhibition_id,
            name,
            summary,
            datetime.fromisoformat(start_at),
            datetime.fromisoformat(finish_at),
        )
    except Exception as e:
        logging.error(e.message)
