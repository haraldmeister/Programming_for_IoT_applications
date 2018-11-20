import cherrypy
import json
import requests


class BikeSharing():
    exposed=True

    @cherrypy.tools.json_out()
    def GET(self,*uri,**params):
        if len(uri)==0:
            self.json_data = requests.get("https://api.citybik.es/v2/networks/to-bike").json()
            return json.loads(json.dumps(self.json_data,default=lambda x: x.__dict__))

        if uri[0]=="order_slots":
            self.json_data = requests.get("https://api.citybik.es/v2/networks/to-bike").json()
            self.json_out=[]

            if "N" in params:
                self.N=int(params["N"])
            else:
                self.N=10
            if "order" in params:
                if params["order"]=="ascend":
                    self.json_data['network']['stations'] = sorted(self.json_data['network']['stations'], key=lambda k: int(k.get('empty_slots', 0)), reverse=False)
                if params["order"]=="descend":
                    self.json_data['network']['stations'] = sorted(self.json_data["network"]["stations"], key=lambda k: int(k.get('empty_slots', 0)), reverse=True)
            else:
                self.json_data['network']['stations'] = sorted(self.json_data["network"]["stations"], key=lambda k: int(k.get('empty_slots', 0)), reverse=True)

            for i in range(0,self.N):
                self.json_out.append(self.json_data["network"]["stations"][i])

            return json.loads(json.dumps(self.json_out,default=lambda x: x.__dict__))

        if uri[0]=="order_bikes":
            self.json_data = requests.get("https://api.citybik.es/v2/networks/to-bike").json()
            self.json_out=[]

            if "N" in params:
                self.N=int(params["N"])
            else:
                self.N=10
            if "order" in params:
                if params["order"]=="ascend":
                    self.json_data['network']['stations'] = sorted(self.json_data['network']['stations'], key=lambda k: int(k.get('free_bikes', 0)), reverse=False)
                if params["order"]=="descend":
                    self.json_data['network']['stations'] = sorted(self.json_data['network']['stations'], key=lambda k: int(k.get('free_bikes', 0)), reverse=True)
            else:
                self.json_data['network']['stations'] = sorted(self.json_data['network']['stations'], key=lambda k: int(k.get('free_bikes', 0)), reverse=True)

            for i in range(0,self.N):
                self.json_out.append(self.json_data['network']['stations'][i])

            return json.loads(json.dumps(self.json_out,default=lambda x: x.__dict__))


        if uri[0]=="count_bikes_slots":
            self.json_data = requests.get("https://api.citybik.es/v2/networks/to-bike").json()
            self.bikes=0
            self.slots=0

            if "lat" and "lon" in params:
                self.lat=float(params["lat"])
                self.lon=float(params["lon"])
            else:
                return "District number not set"
            for i in range(0,len(self.json_data["network"]["stations"])):
                if ((float(self.json_data["network"]["stations"][i]["latitude"])<self.lat+0.005 and
                    float(self.json_data["network"]["stations"][i]["latitude"])>self.lat-0.005) and
                    (float(self.json_data["network"]["stations"][i]["longitude"])<self.lon+0.01 and
                    float(self.json_data["network"]["stations"][i]["longitude"])>self.lon-0.01)):
                    self.bikes+=int(self.json_data["network"]["stations"][i]["free_bikes"])
                    self.slots+=int(self.json_data["network"]["stations"][i]["empty_slots"])
            self.json_out={"latitude":float(params["lat"]),"longitude":float(params["lon"]),"bikes":self.bikes,"slots":self.slots}
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