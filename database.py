import sqlite3 as dbase
import os.path
import hashlib as hash
import random

db_path = "D:/python/locky/users/locky.sqlite"
table_name = "locky"
base_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
code_len = 9

# --- Sign up exceptions
class UserExist(Exception):
    """Raise if user enter existed username"""
    pass

class UncorrectPwdType(Exception):
    """Raise if user enter uncorrect type of password"""
    pass

class UnknownUser(Exception):
    """Raise if unknown user try to login"""
    pass
# --- End of exceptions


def hashPwd(password, salt):
    hash_str = hash.sha1(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    return hash_str

def isUserExist(username):
    connect = dbase.connect(db_path)
    cursor = connect.cursor()
    cursor.execute("""SELECT Username FROM locky ORDER BY Username""")
    result = cursor.fetchall()
    cursor.close()
    result = [x[0] for x in result]
    if result.count(username) == 0:
        return False
    else:
        return True

def isCorrectPassword(password):
    if len(password) >= 8 and password.isalnum():
        return False
    else:
        return True

def login(username, password):
    if isUserExist(username):
        connect = dbase.connect(db_path)
        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM locky WHERE Username = ?""", [username])
        results = cursor.fetchall()
        if hashPwd(password, results[0][0]) == results[0][2]:
            return True
        else:
            return False
    else:
        raise UnknownUser

class User(object):
    def __init__(self, username, password):
        if isUserExist(username):
            raise UserExist
        elif isCorrectPassword(password):
            raise UncorrectPwdType
        else:
            self.salt = self.salt()
            self.hash = hashPwd(password, self.salt)
            self.username = username
            self.add([self.salt, self.username, self.hash])

    def salt(self):
        str = ""
        for i in range(code_len):
            str += random.choice(base_chars)
        return str

#class DBase(object):
    def add(self, user_data):
        # user_data : turple
        connect = dbase.connect(db_path)
        cursor = connect.cursor()
        cursor.execute("""INSERT INTO locky('UserKey', 'Username', 'Password') VALUES (?, ?, ?)""", user_data)
        connect.commit()
        cursor.close()

    def delete(self):
        connect = dbase.connect(db_path)
        cursor = connect.cursor()
        cursor.execute("""DELETE FROM locky WHERE Username = ?""", [self.username])
        connect.commit()
        cursor.close()

    def edit(self, field, value):
        connect = dbase.connect(db_path)
        cursor = connect.cursor()
        cursor.execute("""UPDATE locky SET {} = {} WHERE Username = {}""".format(field, value, self.username))
        connect.commit()
        cursor.close()



