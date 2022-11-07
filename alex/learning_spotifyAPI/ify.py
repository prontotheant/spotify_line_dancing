"""
file: ify.py
project: playing_with_spotify
author: A. Patterson
purpose: learn to post to spotify api
"""

import json
import requests

if __name__ == '__main__':

    user_id = "prontotheant"
    token = "BQBzkgxSsewqSd5O0BbsQ4iuTDj8V02aiIzgWTeK3ZmZ1NJj2x6IkBHn-rcOBGaaJpTrlk8yHvR2egVR5ae1dz1QgVyfg11cXObPXgIwRnGJ9_BFx4LLPNfisFPxA_b3m7VKBsKPCr3FiDDScLbx8q0Im3daMaJC8ZTj3_4Q3iqdr7ffVfqJZ-JD5ASwEFPkyAtamqHHsIxR-oKd8w"

    endpoint_url = "https://api.spotify.com/v1/recommendations?"

    # variables to pass to api to narrow search
    amount = 11
    country = "US"
    seed_genres = "indie"
    dance_ability = .8

    query = f'{endpoint_url}limit={amount}&market={country}&seed_genres={seed_genres}&target_danceability={dance_ability}'

    response_track = requests.get(query, headers={"Content-Type": "application/json", "Authorization":
        f"Bearer {token}"})

    track_list1 = []
    json_response = response_track.json()
    for track in json_response['tracks']:
        mask = "spotify:track:"
        mask += f"{track['id']}"
        track_list1.append(mask)
        # print(f"{track['name']} by {track['artists'][0]['name']} id: {track['id']}")

    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

    request = json.dumps({
        "name": "Super COOL coding Playlist like 4",
        "description": "My second program generated playlist!!!",
        "public": False  # let's keep it between us - for now
    })

    response = requests.post(url=endpoint_url, data=request, headers={"Content-Type": "application/json",
                                                                      "Authorization": f"Bearer {token}"})

    print(response.status_code)
    playlist_id = response.json()['id']

    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    request = json.dumps({
        "uris": track_list1
    })

    response = requests.post(url=endpoint_url, data=request, headers={"Content-Type": "application/json",
                                                                      "Authorization": f"Bearer {token}"})
    print(response.status_code)

    print(track_list1)
    