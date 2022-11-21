"""
file: spotify_playlist.py
author: A. Patterson
purpose: host function for connection to spotify
"""
import json
import requests


def spot_api_playlist(token, s_username, spot_ids, p_name, p_desc):
    packaged_for_spot = []
    for s_id in spot_ids:
        mask = "spotify:track:"
        mask = mask + f"{s_id}"
        packaged_for_spot.append(mask)

    endpoint_url = f"https://api.spotify.com/v1/users/{s_username}/playlists"

    play_info = json.dumps({
        "name": f"{p_name}",
        "description": f"{p_desc}",
        "public": False
    })

    play = requests.post(url=endpoint_url, data=play_info, headers={"Content-Type": "application/json",
                                                                    "Authorization": f"Bearer {token}"})

    return play.status_code

    #endpoint_url = f"https://api.spotify.com/v1/playlists/{play.json()['id']}/tracks"
    #
    #songs = json.dumps({
    #    "uris": packaged_for_spot
    #})
    #
    #complete = requests.post(url=endpoint_url, data=songs, headers={"Content-Type": "application/json",
    #                                                                "Authorization": f"Bearer {token}"})
    #if complete.status_code == "":
    #    return 1
    #else:
    #    return 0
    #