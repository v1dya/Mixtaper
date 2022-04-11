import spotipy
import os
import spotify_dl
from spotipy.oauth2 import SpotifyClientCredentials

class Song:
    def __init__(self, name, genre, artist):
        self.name = name
        self.genre = genre
        self.artist = artist


def songSelect():
    print('song select')


def mixtapeAlbum(sp):
    # Get list of albums
    albumList = sp.search(q='album:' + input("Enter your album: "), type='album')

    # Album does not exist
    if not albumList['albums']['items']:
        print("Invalid")
        mixtapeAlbum(sp)
        return

    # Select the top most album in list
    album = albumList['albums']['items'][0]

    albumUri = album['id']
    print(albumUri)
    url = 'https://open.spotify.com/album/' + albumUri

def spotifyPlaylist(user):
    print('playlist')


def handleSpotify():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    choice = int(input("1.Select songs\n"
                       "2.Mixtape albums\n"
                       "Enter your choice: "))

    if choice == 1:
        songSelect()
    elif choice == 2:
        mixtapeAlbum(sp)
    else:
        print('invalid input')
        handleSpotify()
        return
