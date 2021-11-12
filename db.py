import sqlite3


class DB_manager:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def add_user_referal(self, user_id, referal):
        with self.connection:
            self.cursor.execute("INSERT INTO `users` (`User_Id`, `Working_State`, `Referal`) VALUES (?, ?, ?)",
                                (user_id, "start", referal,))

    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO users(User_Id, Working_State) VALUES(?, ?)",
                                (user_id, "start",))

    def exists_user(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `User_Id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def get_user_state(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `Working_State` FROM `users` WHERE `User_Id` = ?",
                                         (user_id,)).fetchall()
            for row in result:
                working_state = str(row[0])
            return working_state

    def get_user_language(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `Language` FROM `users` WHERE `User_Id` = ?", (user_id,)).fetchall()
            for row in result:
                language = str(row[0])
            return language

    def get_user_email(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `Email` FROM `users` WHERE `User_Id` = ?", (user_id,)).fetchall()
            for row in result:
                email = str(row[0])
            return email

    def set_user_language(self, user_id, language):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `Language` = ? WHERE `User_Id` = ?",
                                       (language, user_id,))

    def set_user_working_state(self, user_id, state):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `Working_State` = ? WHERE `User_Id` = ?",
                                       (state, user_id,))

    def exists_verificate_email(self, email):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `Email` = ? AND `Working_State` = ?",
                                         (email, "verificate",)).fetchall()
            return bool(len(result))

    def set_user_email(self, user_id, email):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `Email` = ? WHERE `User_Id` = ?", (email, user_id,))

    def set_user_email_code(self, email, code):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `Email_Code` = ? WHERE `Email` = ?", (code, email,))

    def get_user_email_code(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `Email_Code` FROM `users` WHERE `User_Id` = ?", (user_id,)).fetchall()
            for row in result:
                code = str(row[0])
            return code

    def set_user_referal_link(self, user_id, referal_link):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `Referal_Link` = ? WHERE `User_Id` = ?", (referal_link, user_id,))

    def get_count_referals(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `Referal` = ? AND `Working_State` = ?", (user_id, "verificate",)).fetchall()
            return len(result)

    def set_user_referal(self, user_id, referal):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `Referal` = ? WHERE `User_Id` = ?", (referal, user_id,))

    def get_user_referal_link(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `Referal_Link` FROM `users` WHERE `User_Id` = ?", (user_id,))
            for row in result:
                link = str(row[0])
            return link