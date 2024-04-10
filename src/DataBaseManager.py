import logging
import sqlite3
from datetime import datetime


class DBManager:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addUser(self, nickname, login, password, email):
        try:
            self.__cur.execute(f'INSERT INTO Users (nickname, login, password, email, date_joined) VALUES ({nickname}, {login}, {password}, {email}, {datetime.now()})')
            logging.info(f'User register: {nickname}, {login}, {password}, {email}')
            return True
        except sqlite3.Error as e:
            logging.error(f'Sqlite3 error: {e}')
        finally:
            return False

    def getUser(self, user_id):
        try:
            self.__cur.execute(f'SELECT * FROM Users WHERE id = {user_id} LIMIT 1')
            res = self.__cur.fetchone()
            if not res:
                logging.error(f"User don't found: {user_id}")
                return False
            return res
        except sqlite3.Error as e:
            logging.error(f"Sqlite3 error: {e}")
        finally:
            return False
