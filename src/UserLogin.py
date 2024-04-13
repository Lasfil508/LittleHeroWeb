class UserLogin:
    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(selfs):
        return True

    def is_anonymuos(self):
        return False

    def get_id(self):
        return str(self.__user['id'])

    def get_nickname(self):
        print(self.__user)
        return str(self.__user['nickname'])
