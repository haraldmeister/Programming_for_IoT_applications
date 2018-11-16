import cherrypy
import json

class Freeboard(object):
    exposed=True
    def GET(self,*uri,**params):
        return open("./freeboard/index.html","r").read()
class Save(object):
    exposed=True
    def POST(self,*uri,**params):
        data=json.loads(params['json_string'])
        with open("./freeboard/dashboard/dashboard.json", "w") as f:
           json.dump(dash, f)  # Write json to file


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.staticdir.root':"C:/Users/Edoardo/Documents/PycharmProjects/Programming_for_IoT_applications/lab2/freeboard"
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "css"
        },
        '/dashboard': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "dashboard"
        },
        '/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "js"
        },
        '/img': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "img"
        },
        '/plugins': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "plugins"
        },
    }
    cherrypy.tree.mount(Freeboard(), '/', conf)
    cherrypy.tree.mount(Save(), '/save', conf)
    
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
