import cherrypy
import os.path
from jinja2 import Environment, PackageLoader, select_autoescape

from client import *


#Lista com todas as informações de todos os clientes
clientDatabase = []
#lista com todas as informações de todos os produtos
productsDatabase = []
#Lista com os produtos presentes no carrinho
productsCar = []

fillDataBase(productsDatabase)

# The absolute path to this file's base directory:
baseDir = os.path.dirname(os.path.abspath(__file__))

#Dicionário com a configuração da aplicação
conf = {
  'global': {'tools.sessions.on': True,
            'server.socket_host': '0.0.0.0',
            'server.socket_port': int(os.environ.get('PORT', 5000)), },
  "/":     {'tools.sessions.on': True, 
            "tools.staticdir.root": baseDir },
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
    def logout(self):
      productsCar.clear()
      tparams = {
        'errors': False
      }
      return self.render('login.html', tparams)

    @cherrypy.expose
    def main(self):
      tparams = {
        'num': len(productsCar)
      }
      return self.render('index.html', tparams)
    
    @cherrypy.expose
    def product(self):
      tparams = {
        'products': productsDatabase,
        'num': len(productsCar)
      }
      return self.render('product.html', tparams)
    
    @cherrypy.expose
    def services(self):
      tparams = {
        'num': len(productsCar)
      }
      return self.render('services.html', tparams)
    
    @cherrypy.expose
    def about(self):
      tparams = {
        'num': len(productsCar)
      }
      return self.render('about.html', tparams)
    
    @cherrypy.expose
    def contact(self):
      tparams = {
        'num': len(productsCar)
      }
      return self.render('contact.html', tparams)
    
    @cherrypy.expose
    def register(self):
      tparams = {
        'errors': False
      }
      return self.render('register.html', tparams)
    
    @cherrypy.expose
    def oficina(self):
      tparams = {
        'num': len(productsCar)
      }
      return self.render('oficina.html', tparams)
    
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
    def single(self, pn=None):
      for p in productsDatabase:
        if pn == p.name:
          tparams = {
            'productname': p.name,
            'price': p.price,
            'productinfo': p.info0,
            'productinfo2': p.info1,
            'country': p.country,
            'marca': p.brand,
            'modelo': p.model,
            'peso': p.weight,
            'unidades': p.unidades,
            'cond': p.cond,
            'comments': p.comments,
            'imgsrc': p.img,
            'num': len(productsCar)
          }
          return self.render('single.html', tparams)
      return None

    @cherrypy.expose
    def additem(self, pname=None):
      for p in productsDatabase:
        if pname == p.name:
          productsCar.append(p)
      tparams = {
        'products': productsDatabase,
        'num': len(productsCar)
      }
      return self.render('product.html', tparams)

    @cherrypy.expose
    def cart(self):
      total = 0
      for product in productsCar:
        total+=product.price
      tparams = {
        'carproducts': productsCar,
        'total': total,
        'num': len(productsCar)
      }
      return self.render('cart.html', tparams)

    @cherrypy.expose
    def empty(self):
      productsCar.clear()
      tparams = {
        'num': len(productsCar)
      }
      return self.render('cart.html', tparams)
    
    @cherrypy.expose
    def payment_done(self, firstname=None, email=None, address=None, city=None, state=None, zip=None, cardname=None, cardnumber=None, expmonth=None, expyear=None, cvv=None, sameadr=None):
      productsCar.clear()
      tparams = {
        'num': len(productsCar)
      }
      return self.render('done.html', tparams)
    
    @cherrypy.expose
    def user(self):
      productsCar.clear()
      tparams = {
        'num': len(productsCar)
      }
      return self.render('user.html', tparams)

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '127.0.0.1'})
    cherrypy.quickstart(HelloWorld(), "/", conf)