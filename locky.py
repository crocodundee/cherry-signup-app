# --- Import modules
import pages as part
#import logs as user
import os, os.path
import cherrypy
import database as db
import sqlite3 as dbase
from cherrypy.lib import auth_basic

# --- Jinja2 config
from jinja2 import FileSystemLoader, Environment
file_loader = FileSystemLoader("../locky")
env = Environment(loader = file_loader)

# -- Load templates
index_html = env.get_template("/static/index.html")
login_html = env.get_template("/static/login.html")
error_html = env.get_template("/static/error.html")
control_html = env.get_template("/static/control.html")
signup_html = env.get_template("/static/signup.html")
locky_ctrl_html = env.get_template("/static/locky_control.html")

class Locky(object):
    @cherrypy.expose
    def index(self):
        return index_html.render(content = part.content)

class Control(object):
    @cherrypy.expose
    def index(self):
        return control_html.render()#content = part.control_panel)

class Login(object):
    @cherrypy.expose
    def index(self):
        return login_html.render(content = part.form)

    @cherrypy.expose
    def control(self, username, password):
        """Here is place for user's session confirm"""
        try:
            if db.login(username, password):
                raise cherrypy.HTTPRedirect("/control/")
            else:
                return login_html.render(content=part.form, result="Uncorrect username or password")
        except db.UnknownUser:
            return login_html.render(content=part.form, result="Please sign up")

class SignUp(object):
    @cherrypy.expose
    def index(self):
        return signup_html.render(content = part.reg_form)

    @cherrypy.expose
    def welcome(self, username, password, confirm):
        if password == confirm:
            try:
                user = db.User(username, password)
            except db.UserExist:
                return signup_html.render(content = part.reg_form, result = "User with this name is already exist")
            except db.UncorrectPwdType:
                return signup_html.render(content = part.reg_form, result = "Uncorrect password type")
            else:
                raise cherrypy.HTTPRedirect("/control/")
        else:
            return signup_html.render(content=part.reg_form, result = "Confirm your password")

class LockyControl(object):
    @cherrypy.expose
    def index(self):
        return locky_ctrl_html.render(content = part.switch)

    @cherrypy.expose
    def light(self, ledState):
        if ledState == 'ON':
            action = "<h2 style=\"text-align: center;\">Light is on</h2>"
            #lightOn()
        else:
            action = "<h2 style=\"text-align: center;\">Light is off</h2>"
            #lightOff()
        return locky_ctrl_html.render(content = part.switch, result = action)#content = part.control_panel)

#    @cherrypy.expose
#    def reset(self, reset):
#        raise cherrypy.HTTPRedirect("/control/")
        #return locky_ctrl_html.render(content = part.switch, result = "Waiting your action")#content = part.control_panel)

if __name__ == "__main__":

    config = {
        '/style':
            {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'D:\python\locky\style'
            },
        '/static':
            {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'D:\python\locky\static',
                'tools.staticdir.index': 'index.html'
            },
        '/protected/area':
            {
                'tools.auth_basic.on': True,
                'tools.auth_basic.realm': 'localhost',
                'tools.auth_basic.checkpassword': Login.control,
                'tools.auth_basic.accept_charset': 'UTF-8',
            },
        '/favicon.ico':
            {
                'tools.staticfile.on': True,
                'tools.staticfile.filename': "D:\python\locky\img\locky.ico"
            }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})

    cherrypy.tree.mount(Locky(), '/', config=config)
    cherrypy.tree.mount(Control(), '/control')
    cherrypy.tree.mount(LockyControl(), "/control/locky-control/")
    cherrypy.tree.mount(Login(), '/login')
    cherrypy.tree.mount(SignUp(), '/reg')

    cherrypy.engine.start()
    cherrypy.engine.block()
