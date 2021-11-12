import smtplib
import os
from config import EMAIL
from config import PASSWORD
from config import DBFILE
import random
import string
from email.mime.text import MIMEText
from db import DB_manager
import logging


class Verificator:
    def __init__(self):
        self.sender = EMAIL
        self.pas = PASSWORD
        self.db = DB_manager('data/'+DBFILE)

    def send_code(self, user_email) -> bool:
        code = self.__generate_code()
        server = smtplib.SMTP("smtp.gmail.com: 587")
        server.starttls()
        try:
            server.login(self.sender, self.pas)
            msg = MIMEText(code)
            msg["Subject"] = "Code HERE!!!"
            server.sendmail(self.sender, user_email, msg.as_string())
            self.db.set_user_email_code(user_email, code)
            server.quit()
            return True
        except Exception:
            logging.error(Exception, exc_info=True)
            return False

    def __generate_code(self) -> str:
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.sample(letters_and_digits, 5))

    def check_code(self, user_id, user_code) -> bool:
        if self.db.get_user_email_code(user_id) == user_code:
            user_email = self.db.get_user_email(user_id)
            self.db.set_user_email_code(user_email, "NANI")
            return True
        else:
            return False