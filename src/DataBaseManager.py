import logging
import sqlite3
from datetime import datetime


class DBManager:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addUser(self, nickname, password, email):
        try:
            self.__cur.execute(f'INSERT INTO Users VALUES(NULL, ?, ?, ?, ?)', (nickname, password, email, datetime.now()))
            self.__db.commit()
            logging.info(f'User register: {nickname}, {password}, {email}')
            return True
        except sqlite3.Error as e:
            logging.error(f'Sqlite3 error: {nickname}, {email}, {password}, {e}')
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
        return False

    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM Users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                logging.error(f"User don't found: {email}")
                return False
            return res
        except sqlite3.Error as e:
            logging.error(f"Sqlite3 error: {e}")
        return False
