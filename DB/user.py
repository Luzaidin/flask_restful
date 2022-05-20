from .indexDB import DB

class UserCollection(DB):
    def __init__(self):
        self.table_name = 'user'
        self.fields = ('name', 'email')
    
    def createUser(self, name, email):
        self.initCursor()
        self.cursor.execute(f"INSERT INTO {self.table_name} (name, email) VALUES ('{name}', '{email}')")
        self.commitConnection()
        self.closeCursor()
        self.closeConnection()

    def readUser(self):
        self.initCursor()
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        data = self.cursor.fetchall()
        self.closeCursor()
        self.closeConnection()
        return data

    def listUser(self, id):
        self.initCursor()
        self.cursor.execute(f'SELECT * FROM {self.table_name} WHERE _id = {id}')
        data = self.cursor.fetchall()
        self.closeCursor()
        self.closeConnection()
        return data

    def updateUser(self, id, name, email):
        self.initCursor()
        self.cursor.execute(f"UPDATE {self.table_name} SET name = '{name}', email = '{email}' WHERE _id = {id}")
        self.commitConnection()
        self.closeCursor()
        self.closeConnection()

    def deleteUser(self, id):
        self.initCursor()
        self.cursor.execute(f'DELETE FROM {self.table_name} WHERE _id = {id}')
        self.commitConnection()
        self.closeCursor()
        self.closeConnection()