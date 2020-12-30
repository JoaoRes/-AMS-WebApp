import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
      return  """
       uzapains
"""
    
    @cherrypy.expose
    def new(self):
        return "bye world"


if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
