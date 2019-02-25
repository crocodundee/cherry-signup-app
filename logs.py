import os, os.path
import random
import string

users_env = "D:\\python\\locky\\users\\login.txt"
base_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
code_len = 9

def getUserCode():
    str = ""
    for i in range(code_len):
        str += random.choice(base_chars)
    return str

def getUserNames():
    all_users = list()
    with open(users_env) as names:
        for n in names:
            user_data = n.split("/")
            all_users.append(user_data[1])
    return all_users

def getUserPwd():
    all_users_pwd = list()
    with open(users_env) as passwords:
        for pwd in passwords:
            user_data = pwd.split("/")
            all_users_pwd.append(user_data[2])
    return all_users_pwd

def isCorrectPassword(password):
    if len(password) >= 8 and password.isalnum():
        return True
    else:
        return False

def isUserExist(username):
    if getUserNames().count(username):
        return True
    else:
        return False

def isUsersPassword(username, password):
    with open(users_env) as data:
        for d in data:
            user_data = d.split("/")
            if (user_data[1] == username):
                pwd = user_data[2].split("\n")
                if pwd[0] == password:
                    return True
                else:
                    return False

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.code = getUserCode()
        new_user = open(users_env, "a")
        new_user.write(self.code + "/" + self.username + "/" + self.password + "\n")
