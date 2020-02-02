import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

session = spotipy.Spotify(
   client_credentials_manager=SpotifyClientCredentials()
   )

def play( query ):
   pass

def __search():
   res = ""