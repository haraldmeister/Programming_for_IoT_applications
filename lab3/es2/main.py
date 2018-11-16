import requests
import json
while True:
    print("Welcome to Discography service\nChoose your operation:\n")
    print("1 Search by artist\n2 Search by album title\n3 Search by year\n")
    print("4 Search by number of songs\n5 Print discography\n6 Insert album\n")
    print("7 Delete album\n")
    a=input()

    if a=="quit":
        print("Quitting program....")
        break

    ch=int(a)

    if ch==1:
        artist=input("Name of the artist\n")
        result=requests.get("http://localhost:9090/search_artist/"+artist).json()
        #json_data=json.loads(result)
    elif ch==2:
        title=input("Name of the album\n")
        result=requests.get("http://localhost:9090/search_title/"+title).json()
        #json_data=json.loads(result)
    elif ch==3:
        album=input("Year of the album\n")
        result=requests.get("http://localhost:9090/search_title/"+album).json()
    elif ch==4:
        n_song=input("Number of song in the album\n")
        result=requests.get("http://localhost:9090/search_title/"+n_song).json()
        #json_data=json.loads(result)
    elif ch==5:
        result=requests.get("http://localhost:9090/").json()
        #json_data=json.loads(result)
    elif ch==6:
        artist=input("Name of the artist\n")
        title=input("Name of the album\n")
        year=input("Year of the album\n")
        n_song=input("Number of song in the album\n")
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        json_input={"artist":artist,"title":title,"year":int(year),"N":int(n_song)}
        result=requests.post("http://localhost:9090/insert_album/",data=json.dumps(json_input),headers=headers)

    elif ch==7:
        artist=input("Name of the artist\n")
        title=input("Name of the album\n")
        year=input("Year of the album\n")
        n_song=input("Number of song in the album\n")
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        json_input={"artist":artist,"title":title,"year":int(year),"N":int(n_song)}
        result=requests.post("http://localhost:9090/delete_album/",data=json.dumps(json_input),headers=headers)

    if ch<5:
        print("\nArtist: %s" % result["Artist"])
        print("Album title: %s " % result["Title"])
        print("Year: %d" % result["Year"])
        print("Number of songs: %d\n" % result["Total songs"])
    if ch==5:
        for j in range(len(result['Album List'])):
            print("\nAlbum %d\nArtist: %s\nAlbum title: %s\nYear: %s\nNumber of songs: %s\n" % (j+1,result['Album List'][j]['artist'],
                                             result['Album List'][j]['year'],
                                             result['Album List'][j]['title'],
                                             result['Album List'][j]['N']))
    else:
        continue
