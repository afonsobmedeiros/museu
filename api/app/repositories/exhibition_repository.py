from datetime import datetime
from database.connections import get_connection


def create(
    name: str, summary: str, start_at: datetime, finish_at: datetime, curator_id: int
) -> int:
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO MUSEU.Exhibitions"
        sql += " (Id, Name, Summary, Start_at, Finish_at, Created_at, Updated_at, CuratorId)"
        sql += " VALUES(null, %s, %s, %s, %s, current_timestamp(), current_timestamp(), %s);"
        cursor.execute(sql, (name, summary, start_at, finish_at, curator_id))
        result = cursor.lastrowid
        connection.commit()
    if result:
        return result
    return None


def create_many(exhibitions: list[dict]) -> int:
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO MUSEU.Exhibitions"
        sql += " (Id, Name, Summary, Start_at, Finish_at, Created_at, Updated_at, CuratorId)"
        sql += " VALUES(null, %s, %s, %s, %s, current_timestamp(), current_timestamp(), %s);"
        result = cursor.executemany(sql, exhibitions)
        connection.commit()
    if result:
        return result
    return None


def update(
    exhibition_id: int,
    name: str,
    summary: str,
    start_at: datetime,
    finish_at: datetime,
):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "UPDATE MUSEU.Exhibitions"
        sql += " SET Name=%s, Summary=%s, Start_at=%s, Finish_at=%s"
        sql += " WHERE Id=%s;"
        result = cursor.execute(
            sql, (name, summary, start_at, finish_at, exhibition_id)
        )
        connection.commit()
    if result:
        return result
    return None
