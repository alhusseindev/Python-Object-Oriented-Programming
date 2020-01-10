import requests


class Music:
    def __init__(self, artist_name=None, album_name=None, song_name=None):

        self.artist_name=artist_name
        self.album_name=album_name
        self.song_name=song_name

    def __str__(self):
        return "Artist Name: {}, Album Name: {}, Song Name: {}".format(self.artist_name,self.album_name, self.song_name)

    #setters
    def artist_name_setter(self,artist_name):
        self.artist_name=artist_name
    def album_name_setter(self,album_name):
        self.album_name=album_name
    def song_name_setter(self, song_name):
        self.song_name=song_name

    #Getters    
    def get_artist_name(self):
        return self.artist_name
    def get_album_name(self):
        return self.album_name
    def get_song_name(self):
        return self.song_name

    
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

#    print(artist_name)
#    print(album_name)




#Question 5

def search(artist_name):
    for song in top_songs:
        if song.get_artist_name() == artist_name:
            print(song)
    return


search("Taylor Swift")


#Name: Alhussein Eweis
