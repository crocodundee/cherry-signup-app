import os, os.path
import cherrypy

# --- Jinja2 config
from jinja2 import FileSystemLoader, Environment
file_loader = FileSystemLoader("../locky")
env = Environment(loader = file_loader)
template = env.get_template("/template/index.html")

class Locky(object):
    @cherrypy.expose
    def index(self):
        return template.render()


if __name__ == "__main__":
    config = {
        '/style':
            {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'D:\python\locky\style'
            }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(Locky(), '/', config=config)