import spotipy
import spotdl
from spotipy.oauth2 import SpotifyClientCredentials


def mixtapePlaylist(sp, user):
    externalUrls = user['external_urls']
    uri = user['uri']
    playlist = sp.playlist(playlist_id=uri)
    print(playlist)


def createMixtape(user):
    print('create')


def spotifyPlaylist(user):
    print('playlist')


# d5o7fm1kukg92xsr6fur6smhr
def spotify():
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    username = input('Enter your spotify userID (you can find it in your account page):\n')
    user = sp.user(username)
    print(sp.current_user_followed_artists(limit=1))
    choice = input("1.Mixtape your playlist\n"
                   "2.Mixtape your custom songs\n"
                   "3.Create a new spotify playlist\n"
                   "Enter your choice: ")

    choice = int(choice)

    if choice == 1:
        mixtapePlaylist(user)
    elif choice == 2:
        createMixtape(user)
    elif choice == 3:
        spotifyPlaylist(user)
    else:
        print('invalid input')
