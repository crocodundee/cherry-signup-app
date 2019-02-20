# --- Import modules
import PageGen as part
import os, os.path
import cherrypy
from cherrypy.lib import auth_basic

# --- Jinja2 config
from jinja2 import FileSystemLoader, Environment
file_loader = FileSystemLoader("../locky")
env = Environment(loader = file_loader)

index_html = env.get_template("/static/index.html")
login_html = env.get_template("/static/login.html")
error_html = env.get_template("/static/error.html")
control_html = env.get_template("/static/control.html")

USERS = {'user1' : 'password1'}

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
        if username in USERS and USERS[username] == password:
            return login_html.render(content = part.form , result = "Successefully")
        else:
            return login_html.render(content = part.form , result = "Uncorrect username or password")

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

    cherrypy.engine.start()
    cherrypy.engine.block()