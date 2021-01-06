import cherrypy
import os.path
from jinja2 import Environment, PackageLoader, select_autoescape

from client import *


#Lista com todas as informações de todos os clientes
clientDatabase = []
#lista com todas as informações de todos os produtos
productsDatabase = []

fillDataBase(productsDatabase)

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
      tparams = {
        'products': productsDatabase
      }
      return self.render('product.html', tparams)
    
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
      tparams = {
        'errors': False
      }
      return self.render('register.html', tparams)
    
    @cherrypy.expose
    def testlogin(self, email=None, password=None):
      valid = False
      for client in clientDatabase:
        if client.email == email and client.password == password:
          valid = True

      if valid:
        raise cherrypy.HTTPRedirect("/main")

      tparams = {
        'errors': True
      }
      return self.render('login.html', tparams)

    @cherrypy.expose
    def testregister(self, name=None, password=None, email=None,  address=None):
      c = Client(name, address, email, password)
      
      if c in clientDatabase:
        tparams = {
          'errors': True
        }
        return self.render('register.html', tparams)
      else:
        clientDatabase.append(c)
        raise cherrypy.HTTPRedirect("/main")

    @cherrypy.expose
    def payment(self):
      return open('html/payment.html', 'r')

    
    @cherrypy.expose
    def single(self):
      tparams = {
        'productname': "Radio",
        'price': 4500,
        'productinfo': "A nice yellow radio for your beautifull car",
        'productinfo2': "10 stations, loud speakers, quality sound and other things",
        'country': 'EUA',
        'marca': 'pioneer',
        'modelo': 'XR87',
        'peso': 12,
        'unidades': 9,
        'cond': 'Novo',
        'comments': "O fabricante desta peça recomenda que não a use em certos modelos",
        'imgsrc': "images/product-single-1.jpg"
      }
      return self.render('single.html', tparams)

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), "/", conf)