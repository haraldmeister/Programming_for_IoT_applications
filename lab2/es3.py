import cherrypy
import json


class Calculator():
    def __init__(self):
        self.operands  =[]
        self.operation =[]
        self.result    =[]
        self.instance  ={'operands':[],'operation':[],'result':[]}
    def add(self,operands):
        self.operands  =operands
        self.operation ="Add"
        a=0
        for i in range(0,len(operands)):
            a+=(operands[i])
        self.result                =a
        self.instance['operation'] ='Add'
        self.instance['operands']  =operands
        self.instance['result']    =self.result

    def sub(self,operands):
        self.operands  =operands
        self.operation ="Subtraction"
        a              =operands[0]
        if len(operands)>1:
            for i in range(1,len(operands)):
                a-=operands[i]
        self.result                =a
        self.instance['operation'] ='Subtraction'
        self.instance['operands']  =operands
        self.instance['result']    =self.result

    def mul(self,operands):
        self.operands  =operands
        self.operation ="Multiplication"
        a              =operands[0]
        if len(operands)>1:
            for i in range(1,len(operands)):
                a*=float(operands[i])
        self.result                =a
        self.instance['operation'] ='Multiplication'
        self.instance['operands']  =operands
        self.instance['result']    =self.result

    def div(self,operands):
        self.operands  =operands
        self.operation ="Division"
        a              =operands[0]
        if len(operands)>1:
            for i in range(1,len(operands)):
                try:
                    a/=float(operands[i])
                except ZeroDivisionError:
                    print("Errore divisione per zero\n")
                    self.result=[]
                    self.instance['operation'] ='Division'
                    self.instance['operands']  =operands
                    self.instance['result']    =self.result
                    return
        self.result                =a
        self.instance['operation'] ='Division'
        self.instance['operands']  =operands
        self.instance['result']    =self.result

class add(object):
    exposed = True

    def PUT (self, *uri, **params):
        op=Calculator()
        operands=tuple(float(f) for f in uri)
        op.add(operands)
        return json.dumps(op.instance)

class sub(object):
    exposed = True
    def PUT (self, *uri, **params):
        op=Calculator()
        operands=tuple(float(f) for f in uri)
        op.sub(operands)
        return json.dumps(op.instance)


class mul(object):
    exposed = True
    def PUT (self, *uri, **params):
        op=Calculator()
        operands=tuple(float(f) for f in uri)
        op.mul(operands)
        return json.dumps(op.instance)


class div(object):
    exposed = True
    def PUT (self, *uri, **params):
        op=Calculator()
        operands=tuple(float(f) for f in uri)
        op.div(operands)
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
