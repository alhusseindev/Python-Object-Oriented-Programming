import requests



class Music:
    def __init__(self, artist_name=None, album_name=None, song_name=None):

        self.artist_name=artist_name
        self.album_name=album_name
        self.song_name=song_name

    def __str__(self):
        return "Artist Name: {}, Album Name: {}, Song Name: {}".format(self.artist_name,self.album_name, self.song_name)


    def artist_name_setter(self,artist_name):
        self.artist_name=artist_name
    def album_name_setter(self,album_name):
        self.album_name=album_name
    def song_name_setter(self, song_name):
        self.song_name=song_name
        
    def get_artist_name(self):
        return self.artist_name
    def get_album_name(self):
        return self.album_name
    def get_song_name(self):
        return self.song_name


#Start of Part B
            
class Album:
    def __init__(self, album_name=None):
        self.album_name=album_name
        self.song_names=[]

    def __str__(self):
        return "Album Name: {}, Song Name: {}".format(self.album_name, str(self.song_names)[2:-2])

    def song_name_setter(self, song_name):
        self.song_names.append(song_name)
    
music_entry=Music()
top_songs=[]


url = 'https://itunes.apple.com/us/rss/topsongs/limit=100/json'

response = requests.get(url)

data = response.json()
for artist_dict in data['feed']['entry']:
    artist_name = artist_dict['im:artist']['label']
    album_name = artist_dict['im:collection']['im:name']['label']
    song_name = artist_dict['title']['label']

    if artist_name in song_name:
        song_name=song_name.replace(artist_name,"")
        song_name=song_name[:-2]

    music_entry=Music()
    music_entry.artist_name_setter(artist_name)
    music_entry.album_name_setter(album_name)
    music_entry.song_name_setter(song_name)
    top_songs.append(music_entry)






def search(artist_name):
    album_dict=dict()
    for song in top_songs:
        if song.get_artist_name() == artist_name:
            album_name=song.get_album_name()
            if album_name in album_dict.keys():
                album_dict[album_name].song_name_setter(song.get_song_name())
            else:
                album_name1=Album(album_name)
                album_name1.song_name_setter(song.get_song_name())
                album_dict[album_name]=album_name1

    return album_dict






#Part B - Question 3 

def finder(artist_name):
    print("Artist Name:", artist_name)
    album_dict=search(artist_name)
    for album_name in album_dict.keys():
        print(album_dict[album_name])


            



finder("Taylor Swift")


#Name: Alhussein Eweis


