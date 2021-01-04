import cherrypy
import os.path
from jinja2 import Environment, PackageLoader, select_autoescape

# The absolute path to this file's base directory:
baseDir = os.path.dirname(os.path.abspath(__file__))

#Dicionário com a configuração da aplicação
conf = {
  "/":     { "tools.staticdir.root": baseDir },
  "/js":   { "tools.staticdir.on": True,
             "tools.staticdir.dir": "js" },
  "/css":  { "tools.staticdir.on": True,
             "tools.staticdir.dir": "css" },
  "/html": { "tools.staticdir.on": True,
             "tools.staticdir.dir": "html" },
  "/images":{ "tools.staticdir.on": True,
             "tools.staticdir.dir": "images" },
  "/fonts":{ "tools.staticdir.on": True,
             "tools.staticdir.dir": "fonts" },
}

class HelloWorld(object):
    def __init__(self):
      self.env = Environment(
          loader=PackageLoader('app', 'html'),
          autoescape=select_autoescape(['html', 'xml'])
      )
    
    def render(self, tpg, tps):
      template = self.env.get_template(tpg)
      return template.render(tps)
    
    @cherrypy.expose
    def index(self):
      tparams = {
        'errors': False
      }
      return self.render('login.html', tparams)
    
    @cherrypy.expose
    def main(self):
        return open('html/index.html', 'r')
    
    @cherrypy.expose
    def product(self):
      return open('html/product.html', 'r')
    
    @cherrypy.expose
    def services(self):
      return open('html/services.html', 'r')
    
    @cherrypy.expose
    def about(self):
      return open('html/about.html', 'r')
    
    @cherrypy.expose
    def contact(self):
      return open('html/contact.html', 'r')
    
    @cherrypy.expose
    def register(self):
      return open('html/register.html', 'r')
    
    @cherrypy.expose
    def testlogin(self, email=None, password=None):
      if (email.find('ua.pt') != -1):
        raise cherrypy.HTTPRedirect("/main")

      tparams = {
        'errors': True
      }
      return self.render('login.html', tparams)

    @cherrypy.expose
    def testregister(self, name=None, password=None, email=None,  address=None):
      raise cherrypy.HTTPRedirect("/main")


if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), "/", conf)
