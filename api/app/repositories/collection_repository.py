from datetime import datetime
from database.connections import get_connection


def create(name: str, summary: str, exhibition_id: int) -> int:
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO MUSEU.Collections"
        sql += " (Id, Name, Summary, Created_at, Updated_at, ExhibitionId)"
        sql += " VALUES(null, %s, %s, current_timestamp(), current_timestamp(), %s);"
        cursor.execute(sql, (name, summary, exhibition_id))
        result = cursor.lastrowid
        connection.commit()
    if result:
        return result
    return None


def create_many(collections: list[dict]) -> int:
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO MUSEU.Collections"
        sql += " (Id, Name, Summary, Created_at, Updated_at, CuratorId)"
        sql += " VALUES(null, %s, %s, current_timestamp(), current_timestamp(), %s);"
        result = cursor.executemany(sql, collections)
        connection.commit()
    if result:
        return result
    return None


def update(collection_id: int, name: str, summary: str):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "UPDATE MUSEU.Collections"
        sql += " SET Name=%s, Summary=%s"
        sql += " WHERE Id=%s;"
        result = cursor.execute(sql, (name, summary, collection_id))
        connection.commit()
    if result:
        return result
    return None
