# --- Import modules
import pages as part
import logs as user
import os, os.path
import cherrypy
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

class Locky(object):
    @cherrypy.expose
    def index(self):
        return index_html.render(content = part.content)

class Control(object):
    @cherrypy.expose
    def index(self):
        return control_html.render()

class Login(object):
    @cherrypy.expose
    def index(self):
        return login_html.render(content = part.form)

    @cherrypy.expose
    def control(self, username, password):
        if user.isUsersPassword(username, password):
            raise cherrypy.HTTPRedirect("/control/")
        else:
            return login_html.render(content = part.form , result = "Uncorrect username or password")

class SignUp(object):
    @cherrypy.expose
    def index(self):
        return signup_html.render(content = part.reg_form)

    @cherrypy.expose
    def welcome(self, username, password, confirm):
        check_user = user.getUserNames()
        if (check_user.count(username) == 0):
            if password == confirm:
                if user.isCorrectPassword(password):
                    temp = user.User(username, password)
                    raise cherrypy.HTTPRedirect("/control/")
                else:
                    return signup_html.render(content=part.reg_form, result = "Uncorrect password type")
            else:
                return signup_html.render(content=part.reg_form, result = "Confirm your password")
        else:
            return signup_html.render(content = part.reg_form, result = "User with this name is already exist")

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
    cherrypy.tree.mount(Login(), '/login')
    cherrypy.tree.mount(SignUp(), '/reg')

    cherrypy.engine.start()
    cherrypy.engine.block()