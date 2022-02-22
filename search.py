#!/usr/bin/python3



print ("Content-type:text/html\r\n\r\n")



import requests
import urllib.parse
import cgi , cgitb

cgitb.enable()
form = cgi.FieldStorage()
song = form.getvalue('song')





SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/search'
ACCESS_TOKEN = 'BQDO0BZqeEpvB13fZRwH_g7BH6r5mg_V8q3nZF43MHbgBuTFyaMyRuj15fExeOA44mXs19GPJykGf_AMYTu2ZO5s-ALbXldGKMJrzeUibLnyW-v7my6hhPs_1FlYyDmnvxVFFdVsAHHIA1RD3Hv-Sz5gdkzPGeCsy3whFG3190_L2lM9qOocKKDkHSCE-FP6cg4Z4WHPxbUTsi-Ra99Rlqv2EfdSsvmu'
def search_song(song):
    query = urllib.parse.quote(f'{song}')
    url = f'https://api.spotify.com/v1/search?q={query}&type=track'
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    response_json = response.json()

    results = response_json['tracks']['items']
    if results:
        # ppsmol = f"{results[0]['id']} + {results[0]['name']}"
        # return ppsmol
        return results[0]['id']
    else:
        raise Exception(f"No song found for = {song}")


# print ("song is : %s"%song )

def add_song_to_playlist(song_id):
    mystring = "spotify:track:"
    #playlistID = '5D2Zq1vtFW2STgVVjjd9Lo'
    url = f"https://api.spotify.com/v1/playlists/5SaJDvzhqjDD1oNTxMpxyP/tracks"
    response = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            # "ids": [song_id]
            # "uris": ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh"]
            "uris": [mystring + song_id]
        }
    )
    return response.json()

def main():
    
    oghnia = search_song(song)
    added = add_song_to_playlist(oghnia)
    

if __name__ == '__main__':
    main()


print("<html><head><meta http-equiv='refresh' content='1; url=http://127.0.0.1/<!DOCTYPE html>.html'></head> <body> Redirecting...</body></html>")

