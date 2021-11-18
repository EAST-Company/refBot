import sqlite3


if __name__ == "__main__":
    connection = sqlite3.connect('database.db', check_same_thread=False)
    cursor = connection.cursor()
    # Get all user with @gmail
    with connection:
        request = cursor.execute("SELECT `Email` FROM `users` WHERE `Email` like '%gmail%'").fetchall()
        for row in request:
            text = str(row[0]).split('@')
            mes = text[0].replace('.', '')
            print(mes + "@" + text[1])
            print(str(row[0]))
            cursor.execute("UPDATE users SET Email = ? WHERE Email = ?", (mes + "@" + text[1], str(row[0]),))