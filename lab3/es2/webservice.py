import json
import time
import cherrypy

class albums:
    def __init__(self,artist,year,title,num):
        self.artist=artist
        self.year=year
        self.title=title
        self.N=num


class owner(albums):
    def __init__(self,nome,date):
        self.album_list=[]
        self.nome=nome
        self.last_upd=date

        self.result={"Artist":[],"Year":[],"Title":[],"Total songs":[]}
        self.discography={"Owner":self.nome,"Last update":self.last_upd,"Album List":self.album_list}
    def search_artist(self,key_artist):
        for i in range(len(self.album_list)):
            if(str(self.album_list[i].artist)==key_artist):
                self.result["Artist"]=self.album_list[i].artist
                self.result["Year"]=self.album_list[i].year
                self.result["Title"]=self.album_list[i].title
                self.result["Total songs"]=self.album_list[i].N
                return self.result
        return self.result
    def search_title(self,key_title):
        for i in range(len(self.album_list)):
            if(str(self.album_list[i].title)==key_title):
                self.result["Artist"]=self.album_list[i].artist
                self.result["Year"]=self.album_list[i].year
                self.result["Title"]=self.album_list[i].title
                self.result["Total songs"]=self.album_list[i].N
                return self.result
        return self.result
    def search_year(self,key_year):
        for i in range(len(self.album_list)):
            if(str(self.album_list[i].year)==key_year):
                self.result["Artist"]=self.album_list[i].artist
                self.result["Year"]=self.album_list[i].year
                self.result["Title"]=self.album_list[i].title
                self.result["Total songs"]=self.album_list[i].N
                return self.result
        return self.result
    def search_totalsong(self,key_nsong):
        for i in range(len(self.album_list)):
            if(str(self.album_list[i].N)==key_nsong):
                self.result["Artist"]=self.album_list[i].artist
                self.result["Year"]=self.album_list[i].year
                self.result["Title"]=self.album_list[i].title
                self.result["Total songs"]=self.album_list[i].N
                return self.result
        return self.result
    def insert_album(self,artist,year,title,num):
        for i in range(len(self.album_list)):
            if(str(self.album_list[i].artist)==artist and str(self.album_list[i].title)==title ):
                self.album_list[i].N=num
                self.album_list[i].year=year
                self.last_upd=time.strftime('%d/%m/%Y')+' '+time.strftime('%H:%M:%S')
                return
        self.album_list.append(albums(artist,year,title,num))
        self.last_upd=time.strftime('%d/%m/%Y')+' '+time.strftime('%H:%M:%S')
    def print_all(self):
        return self.discography
class Discography(owner):
    exposed=True
    def __init__(self):
        json_data=open("discography.txt").read()
        data = json.loads(json_data)
        self.discogr=owner(data['discography_owner'],data['last_update'])
        for j in range(len(data['album_list'])):
            self.discogr.album_list.append(albums(data['album_list'][j]['artist'],
                                             data['album_list'][j]['publication_year'],
                                             data['album_list'][j]['title'],
                                             data['album_list'][j]['total_tracks']))
    def GET(self,*uri,**params):
        if uri[0]=="search_artist":
            return json.dumps(self.discogr.search_artist(uri[1]))
        if uri[0]=="search_title":
            return json.dumps(self.discogr.search_title(uri[1]))
        if uri[0]=="search_year":
            return json.dumps(self.discogr.search_year(uri[1]))
        if uri[0]=="search_totalsong":
            return json.dumps(self.discogr.search_totalsong(uri[1]))
        if uri[0]=="print":
            return json.dumps(self.discogr.print_all())

    # def POST(self,*uri,**params):
    #     if uri[0]=="insert_album":


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(Discography(), '/', conf)

    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 9090})
    cherrypy.engine.start()
    cherrypy.engine.block()