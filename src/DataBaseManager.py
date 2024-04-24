import logging
import sqlite3
from datetime import datetime


class DBManager:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addUser(self, nickname, password, email, filename):
        try:
            self.__cur.execute(f'INSERT INTO Users VALUES(NULL, ?, ?, ?, ?, ?)', (nickname, password, email, filename, datetime.now()))
            self.__db.commit()
            logging.info(f'User register: {nickname}, {password}, {email}, {filename}')
            return True
        except sqlite3.Error as e:
            logging.error(f'Sqlite3 error: {nickname}, {email}, {password}, {filename}, {e}')
            return e.args[0]

    def addMap(self, user_id, name, description, map_text):
        try:
            self.__cur.execute(f'INSERT INTO Maps VALUES(NULL, ?, ?, ?, ?, ?)', (name, description, map_text, user_id, datetime.now()))
            self.__db.commit()
            self.__cur.execute(f'SELECT MAX(id) FROM Maps')
            res = self.__cur.fetchone()
            logging.info(f'The {res[0]} map was added by the user {user_id}')
            return True
        except sqlite3.Error as e:
            logging.error(f'Sqlite3 error: {e}')
            return e.args[0]

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

    def getMaps(self):
        try:
            self.__cur.execute(f"SELECT * FROM Maps")
            res = self.__cur.fetchall()
            if not res:
                logging.error(f"Maps don't found!")
                return False
            return res
        except sqlite3.Error as e:
            logging.error(f"Sqlite3 error: {e}")
        return False

    def getMap(self, map_id):
        try:
            self.__cur.execute(f"SELECT * FROM Maps WHERE id = {map_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                logging.error(f"Map don't found! {map_id}")
                return False
            return res
        except sqlite3.Error as e:
            logging.error(f"Sqlite3 error: {e}")
        return False
