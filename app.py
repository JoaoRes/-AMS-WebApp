import cherrypy
import os.path

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
    @cherrypy.expose
    def login(self):
      return open('html/login.html', 'r')
    
    @cherrypy.expose
    def index(self):
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



if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), "/", conf)
