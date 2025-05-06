from datetime import datetime
from database.connections import get_connection


def create(subtitle: str, summary: str, part_date: datetime, photo: str, photoPath: str, collection_id: int) -> int:
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO MUSEU.Pieces"
        sql += " (Id, Subtitle, Summary, PartDate, photo, photoPath, CollectionId)"
        sql += " VALUES(null, %s, %s, %s, %s, %s, %s);"
        cursor.execute(sql, (subtitle, summary, part_date, photo, photoPath, collection_id))
        result = cursor.lastrowid
        connection.commit()
    if result:
        return result
    return None


def create_many(pieces: list[dict]) -> int:
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO MUSEU.Pieces"
        sql += " (Id, Subtitle, Summary, PartDate, photo, photoPath, CollectionId)"
        sql += " VALUES(null, %s, %s, %s, %s, %s, %s);"
        result = cursor.executemany(sql, pieces)
        connection.commit()
    if result:
        return result
    return None


def update(piece_id: int, subtitle: str, summary: str, part_date: datetime, photo: str, photo_path: str):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = " UPDATE MUSEU.Pieces"
        sql += " SET Subtitle='', Summary=%s, PartDate=%s, photo=%s, photoPath=%s"
        sql += " WHERE Id=%s;"
        result = cursor.execute(sql, (subtitle, summary, part_date, photo, photo_path, piece_id))
        connection.commit()
    if result:
        return result
    return None
