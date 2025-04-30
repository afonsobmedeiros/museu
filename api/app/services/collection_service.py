from datetime import datetime
from app.repositories import collection_repository as cr


def create(exhibition_id: int, name: str, summary: str) -> int:
    return cr.create(name, summary, exhibition_id)


def update(collection_id: int, name: str, summary: str) -> int:
    return cr.update(collection_id, name, summary)
