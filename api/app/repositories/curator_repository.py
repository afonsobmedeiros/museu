from database.connections import get_connection


def get_curator_by_id(curator_id: int) -> dict:
    """Get user by ID.

    Args:
        curator_id (int): Curator ID

    Returns:
        dict: Dictionary with data user.
    """
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT Id, Name, Email, Password, Type FROM Curators WHERE Id = %s"
        cursor.execute(sql, (curator_id))
        result = cursor.fetchone()

    if result:
        return result
    return None


def get_curator_by_email(email: int):
    """Get user by E-mail

    Args:
        email (int): Curator E-mail

    Returns:
        dict: Dictionary with data user.
    """
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT id, name, email, password, type FROM Curators WHERE Email = %s"
        cursor.execute(sql, (email))
        result = cursor.fetchone()

    if result:
        return result
    return None
