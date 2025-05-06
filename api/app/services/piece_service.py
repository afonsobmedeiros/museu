import logging
from datetime import datetime
from app.repositories import piece_repository as pr


def create(
    subtitle: str,
    summary: str,
    part_date: datetime,
    photo: str,
    photoPath: str,
    collection_id: int,
) -> int:
    try:
        return pr.create(
            subtitle,
            summary,
            datetime.fromisoformat(part_date),
            photo,
            photoPath,
            collection_id,
        )
    except Exception as e:
        logging.error(e.message)


def update(
    piece_id: int,
    subtitle: str,
    summary: str,
    part_date: datetime,
    photo: str,
    photo_path: str,
) -> int:
    try:
        return pr.update(piece_id, subtitle, summary, part_date, photo, photo_path)
    except Exception as e:
        logging.error(e.message)
