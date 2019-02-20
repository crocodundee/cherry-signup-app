import os, os.path
import random
import string

users_env = "D:\\python\\locky\\users\\login.txt"
base_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
code_len = 9

def getUserCode():
    str = ""
    for i in range(code_len):
        str += random.choice(base_str)
    return str

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.code = getUserCode()
        new_user = open(users_env, "a")
        new_user.write(self.code + "/" + self.username + "/" + self.password + "\n")
