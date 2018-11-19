import cherrypy
import json
import requests


class BikeSharing():
    exposed=True

    @cherrypy.tools.json_out()
    def GET(self,*uri,**params):
        if len(uri)==0:
            self.json_data = requests.get("https://www.bicing.cat/"
                                          "availability_map/getJsonObject").json()
            return json.loads(json.dumps(self.json_data,default=lambda x: x.__dict__))

        if uri[0]=="order_slots":
            self.json_data = requests.get("https://www.bicing.cat/"
                                          "availability_map/getJsonObject").json()
            self.json_out=[]

            if "N" in params:
                self.N=int(params["N"])
            else:
                self.N=10
            if "order" in params:
                if params["order"]=="ascend":
                    self.json_data = sorted(self.json_data, key=lambda k: int(k.get('slots', 0)), reverse=False)
                if params["order"]=="descend":
                    self.json_data = sorted(self.json_data, key=lambda k: int(k.get('slots', 0)), reverse=True)
            else:
                self.json_data = sorted(self.json_data, key=lambda k: int(k.get('slots', 0)), reverse=True)

            for i in range(0,self.N):
                self.json_out.append(self.json_data[i])

            return json.loads(json.dumps(self.json_out,default=lambda x: x.__dict__))

        if uri[0]=="order_bikes":
            self.json_data = requests.get("https://www.bicing.cat/"
                                          "availability_map/getJsonObject").json()
            self.json_out=[]

            if "N" in params:
                self.N=int(params["N"])
            else:
                self.N=10
            if "order" in params:
                if params["order"]=="ascend":
                    self.json_data = sorted(self.json_data, key=lambda k: int(k.get('bikes', 0)), reverse=False)
                if params["order"]=="descend":
                    self.json_data = sorted(self.json_data, key=lambda k: int(k.get('bikes', 0)), reverse=True)
            else:
                self.json_data = sorted(self.json_data, key=lambda k: int(k.get('bikes', 0)), reverse=True)

            for i in range(0,self.N):
                self.json_out.append(self.json_data[i])

            return json.loads(json.dumps(self.json_out,default=lambda x: x.__dict__))

        if uri[0]=="get_bike_zip":
            self.json_data = requests.get("https://www.bicing.cat/"
                                          "availability_map/getJsonObject").json()
            self.json_out=[]
            if "zip" in params:
                for i in range(0,len(self.json_data)):
                    if self.json_data[i]["zip"]==params["zip"]:
                        self.json_out.append(self.json_data[i])
            else:
                return "Necessario parametro zip"
            return json.loads(json.dumps(self.json_out,default=lambda x: x.__dict__))

        if uri[0]=="get_electr_bike":
            self.json_data = requests.get("https://www.bicing.cat/"
                                          "availability_map/getJsonObject").json()
            self.json_out=[]
            if "N" in params:
                self.N=int(params["N"])
            else:
                self.N=10
            for i in range(0,len(self.json_data)):
                if self.json_data[i]["stationType"]=="ELECTRIC_BIKE" and \
                        int(self.json_data[i]["bikes"])>self.N:
                    self.json_out.append(self.json_data[i])
            return json.loads(json.dumps(self.json_out,default=lambda x: x.__dict__))

        if uri[0]=="count_bikes_slots":
            self.json_data = requests.get("https://www.bicing.cat/"
                                          "availability_map/getJsonObject").json()
            self.bikes=0
            self.slots=0

            if "district" in params:
                self.district=int(params["district"])
            else:
                return "District number not set"
            for i in range(0,len(self.json_data)):
                if int(self.json_data[i]["district"])==self.district:
                    self.bikes+=int(self.json_data[i]["bikes"])
                    self.slots+=int(self.json_data[i]["slots"])
            self.json_out={"district":int(params["district"]),"bikes":self.bikes,"slots":self.slots}
            return json.loads(json.dumps(self.json_out,default=lambda x: x.__dict__))


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(BikeSharing(), '/', conf)

    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 9090})
    cherrypy.engine.start()
    cherrypy.engine.block()