import cherrypy
import os.path
from jinja2 import Environment, PackageLoader, select_autoescape
import requests;
import os;

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
      cherrypy.session['auth'] = False
      tparams = {
        'errors': False
      }
      return self.render('login.html', tparams)
    
    @cherrypy.expose
    def logout(self):
      cherrypy.session['auth'] = False
      cherrypy.session['productsCar'].clear()
      raise cherrypy.HTTPRedirect("/index")

    @cherrypy.expose
    def main(self):
      tparams = {
        'num': len(cherrypy.session['productsCar']) if cherrypy.session['auth'] else 0,
        'auth': True if cherrypy.session['auth'] else False,
        'login': "Log Out" if cherrypy.session['auth'] else "Log In"
      }
      return self.render('index.html', tparams)
    
    @cherrypy.expose
    def product(self):
      if 'auth' not in cherrypy.session:
       cherrypy.session['auth'] = False
       cherrypy.session['productsCar'] = []
    
      res = requests.get('https://dry-meadow-84562.herokuapp.com/api/product/suggestions')
      #print(res.json()['parts']) # arrray de produtos

      tparams = {
        'products': res.json()['parts'],
        'num': len(cherrypy.session['productsCar']) if cherrypy.session['auth'] else 0,
        'auth': True if cherrypy.session['auth'] else False,
        'login': "Log Out" if cherrypy.session['auth'] else "Log In"
      }
      return self.render('product.html', tparams)
    
    @cherrypy.expose
    def search(self, query):
      if 'auth' not in cherrypy.session:
       cherrypy.session['auth'] = False
       cherrypy.session['productsCar'] = []

      res = requests.post('https://dry-meadow-84562.herokuapp.com/api/product/search', json={'query':query})

      print(res.json())

      tparams = {
        'products': res.json()['results'],
        'num': len(cherrypy.session['productsCar']) if cherrypy.session['auth'] else 0,
        'auth': True if cherrypy.session['auth'] else False,
        'login': "Log Out" if cherrypy.session['auth'] else "Log In"
      }
      return self.render('product.html', tparams)
    @cherrypy.expose
    def services(self):
      tparams = {
        'num': len(cherrypy.session['productsCar']) if cherrypy.session['auth'] else 0,
        'auth': True if cherrypy.session['auth'] else False,
        'login': "Log Out" if cherrypy.session['auth'] else "Log In"
      }
      return self.render('services.html', tparams)
    
    @cherrypy.expose
    def about(self):
      tparams = {
        'num': len(cherrypy.session['productsCar']) if cherrypy.session['auth'] else 0,
        'auth': True if cherrypy.session['auth'] else False,
        'login': "Log Out" if cherrypy.session['auth'] else "Log In"
      }
      return self.render('about.html', tparams)
    
    @cherrypy.expose
    def contact(self):
      tparams = {
        'num': len(cherrypy.session['productsCar']) if cherrypy.session['auth'] else 0,
        'auth': True if cherrypy.session['auth'] else False,
        'login': "Log Out" if cherrypy.session['auth'] else "Log In"
      }
      return self.render('contact.html', tparams)
    
    @cherrypy.expose
    def register(self):
      cherrypy.session['auth'] = False
      tparams = {
        'errors': False
      }
      return self.render('register.html', tparams)
    
    @cherrypy.expose
    def oficina(self):
      tparams = {
        'num': len(cherrypy.session['productsCar']) if cherrypy.session['auth'] else 0,
        'auth': True if cherrypy.session['auth'] else False,
        'login': "Log Out" if cherrypy.session['auth'] else "Log In"
      }
      return self.render('oficina.html', tparams)
    
    @cherrypy.expose
    def testlogin(self, email=None, password=None):
      for client in clientDatabase:
        if client.email == email and client.password == password:
          cherrypy.session['auth'] = True
          cherrypy.session['user'] = {'username': client.username, 'email': client.email, 'role': "client"}
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
        cherrypy.session['auth'] = True
        cherrypy.session['productsCar'] = []
        cherrypy.session['user'] = {'username': name, 'email': email, 'role': "client"}
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
            'num': len(cherrypy.session['productsCar']) if cherrypy.session['auth'] else 0,
            'auth': True if cherrypy.session['auth'] else False,
            'login': "Log Out" if cherrypy.session['auth'] else "Log In"
          }
          return self.render('single.html', tparams)
      return None

    @cherrypy.expose
    def additem(self, pname=None):
      if not cherrypy.session['auth']:
        raise cherrypy.HTTPRedirect("/product")

      for p in productsDatabase:
        if pname == p.name:
          cherrypy.session['productsCar'].append(p)
      raise cherrypy.HTTPRedirect("/product")

    @cherrypy.expose
    def cart(self):
      if not cherrypy.session['auth']:
        raise cherrypy.HTTPRedirect("/main")

      total = 0
      for product in cherrypy.session['productsCar']:
        total+=product.price
      tparams = {
        'carproducts': cherrypy.session['productsCar'],
        'total': total,
        'num': len(cherrypy.session['productsCar']),
        'auth': True if cherrypy.session['auth'] else False,
        'login': "Log Out" if cherrypy.session['auth'] else "Log In"
      }
      return self.render('cart.html', tparams)

    @cherrypy.expose
    def empty(self):
      cherrypy.session['productsCar'].clear()
      raise cherrypy.HTTPRedirect("/cart")
    
    @cherrypy.expose
    def payment_done(self, firstname=None, email=None, address=None, city=None, state=None, zip=None, cardname=None, cardnumber=None, expmonth=None, expyear=None, cvv=None, sameadr=None):
      cherrypy.session['productsCar'].clear()
      tparams = {
        'num': len(cherrypy.session['productsCar']),
        'login': "Log Out" if cherrypy.session['auth'] else "Log In",
        'auth': True if cherrypy.session['auth'] else False
      }
      return self.render('done.html', tparams)
    
    @cherrypy.expose
    def user(self):
      if not cherrypy.session['auth']:
        raise cherrypy.HTTPRedirect("/main")
      
      for c in clientDatabase:
        if c.username == cherrypy.session['user']['username']:      
          tparams = {
            'num': len(cherrypy.session['productsCar']),
            'login': "Log Out" if cherrypy.session['auth'] else "Log In",
            'auth': True if cherrypy.session['auth'] else False,
            'username': c.username,
            'email': c.email,
            'address': c.address
          }
          return self.render('user.html', tparams)

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '127.0.0.1'})
    cherrypy.quickstart(HelloWorld(), "/", conf)