import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from colorama import Fore, Style
from json.decoder import JSONDecodeError

# get username from the terminal
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# User ID: 1232420630?si=oJ4jVWLnQiO1O9PdPCtADg

#erase cache and prompt for user permissions

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

# Create our spotifyObject with permissions
spotifyObject = spotipy.Spotify(auth=token)

# Get current device
devices = spotifyObject.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']

# Current track information
track = spotifyObject.current_user_playing_track()
print()
print(json.dumps(track, sort_keys=True, indent=4))
artist = track['item']['artists'][0]['name']
track = track['item']['name']

if artist != " ":
    print("Currently playing " + track + " by " + artist)

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']
neutral = Style.RESET_ALL
# Prints out json data in a form we can read
# print(json.dumps(VARIABLE, sort_keys=True, indent=4))

while True:
    print()
    print(Fore.RED + Style.BRIGHT + ">>>" + neutral + " Welcome to Spotipy " + displayName + "!")
    print(Fore.RED + Style.BRIGHT + ">>>" + neutral + " You have " + str(followers) + " followers.")
    print()
    print("0 - search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    # Search for the artist
    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?: ")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery, 1, 0, "artist")
        # print(json.dumps(searchResults, sort_keys=True, indent=4))

        #Artists details
        artist = searchResults['artists']['items'][0]
        print(Fore.CYAN + Style.BRIGHT + artist['name'] + neutral)
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        #Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        # Extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        #print(json.dumps(albumResults, sort_keys=True, indent=4))
        albumResults = albumResults['items']

        for item in albumResults:
            print(Style.BRIGHT + Fore.MAGENTA + "Album " + neutral + "\033[4m" + item['name'] + neutral)
            albumID = item['id']
            albumArt = item['images'][0]['url']


            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print(Style.BRIGHT + Fore.BLUE + str(z) + neutral + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()

        #See album art for specific track and play
        while True:
            songSelection = input("Enter a song number to see album art (x to exit): ")
            if songSelection == "x":
                break
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])
            spotifyObject.start_playback(deviceID, None, trackSelectionList)
            webbrowser.open(trackArt[int(songSelection)])
            track = spotifyObject.current_user_playing_track()
            artist = track['item']['artists'][0]['name']
            track = track['item']['name']
            if artist != " ":
                print()
                print("Currently playing " + track + " by " + artist)
            print()
    # End the program
    if choice == "1":
        break
