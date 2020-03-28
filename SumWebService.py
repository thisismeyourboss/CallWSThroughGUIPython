import cherrypy
class SumWebService(object):
    
    @cherrypy.expose
    def webPage(self):
        return "<b> I'm ready! </b>"

    # example of req http://localhost:8080/sum?x=1&y=2&z=3
    @cherrypy.expose
    def sum(self,x,y,z):
        return str(int(x)+int(y)+int(z));       

if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(SumWebService())