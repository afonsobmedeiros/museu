from datetime import datetime
from app.repositories import exhibition_repository as er


def create(
    curator_id: int, name: str, summary: str, start_at: str, finish_at: str
) -> int:
    return er.create(
        name,
        summary,
        datetime.fromisoformat(start_at),
        datetime.fromisoformat(finish_at),
        curator_id,
    )


def update(
    exhibition_id: int,
    name: str,
    summary: str,
    start_at: datetime,
    finish_at: datetime,
):
    return er.update(
        exhibition_id,
        name,
        summary,
        datetime.fromisoformat(start_at),
        datetime.fromisoformat(finish_at),
    )
