import cherrypy
import json


class Calculator():
    def __init__(self):
        self.operand1=[]
        self.operand2=[]
        self.operation=[]
        self.result=[]
        self.instance={'operation':[],'operand1':[],'operand2':[],'result':[]}
    def add(self,operand1,operand2):
        self.operand1=operand1
        self.operand2=operand2
        self.operation="Add"
        self.result=float(operand1)+float(operand2)
        self.instance['operation']='Add'
        self.instance['operand1']=operand1
        self.instance['operand2']=operand2
        self.instance['result']=self.result

    def sub(self,operand1,operand2):
        self.operand1=operand1
        self.operand2=operand2
        self.operation="Subtraction"
        self.result=float(operand1)-float(operand2)
        self.instance['operation']='Subtraction'
        self.instance['operand1']=operand1
        self.instance['operand2']=operand2
        self.instance['result']=self.result
    def mul(self,operand1,operand2):
        self.operand1=float(operand1)
        self.operand2=float(operand2)
        self.operation="Multiplication"
        self.result=float(operand1)*float(operand2)
        self.instance['operation']='Multiplication'
        self.instance['operand1']=float(operand1)
        self.instance['operand2']=float(operand2)
        self.instance['result']=self.result
    def div(self,operand1,operand2):
        self.operand1=operand1
        self.operand2=operand2
        self.operation="Division"
        try:
            self.result=float(operand1)/float(operand2)
        except ZeroDivisionError:
            print("Errore divisione per zero\n")
        self.instance['operation']='Division'
        self.instance['operand1']=operand1
        self.instance['operand2']=operand2
        self.instance['result']=self.result

class add(object):
    exposed = True

    def GET (self, *uri, **params):
        op=Calculator()
        op.add(uri[0],uri[1])
        return json.dumps(op.instance)

class sub(object):
    exposed = True
    def GET (self, *uri, **params):
        op=Calculator()
        op.sub(uri[0],uri[1])
        return json.dumps(op.instance)


class mul(object):
    exposed = True
    def GET (self, *uri, **params):
        op=Calculator()
        op.mul(uri[0],uri[1])
        return json.dumps(op.instance)


class div(object):
    exposed = True
    def GET (self, *uri, **params):
        op=Calculator()
        op.div(uri[0],uri[1])
        return json.dumps(op.instance)

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(add(), '/add', conf)
    cherrypy.tree.mount(sub(), '/sub', conf)
    cherrypy.tree.mount(mul(), '/mul', conf)
    cherrypy.tree.mount(div(), '/div', conf)

    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()