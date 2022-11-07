"""
file: spot.py
project: playing_with_spotify
author: A. Patterson
purpose: learn to use the spotify api
"""

# i would like to add the create a playlist functionality here
# i want to add tracks to the playlist by their ID to check whether or not that is how
# i need to implement the functionality to the website and database


# API stands for application program interface

# APIs allow two or more programs to communicate with each other

# an endpoint is where the API connects to the program

import requests

if __name__ == '__main__':

    # connect to this api ... website api?
    endpoint_url = "https://api.spotify.com/v1/recommendations?"

    # variables to pass to api to narrow search
    amount = 11
    country = "US"
    seed_genres = "indie"
    dance_ability = .8

    token = input("Enter token")

    query = f'{endpoint_url}limit={amount}&market={country}&seed_genres={seed_genres}&target_danceability={dance_ability}'

    response = requests.get(query, headers={"Content-Type": "application/json", "Authorization":
        f"Bearer {token}"})

    json_response = response.json()
    for track in json_response['tracks']:
        # uris.append(track)
        print(f"{track['name']} by {track['artists'][0]['name']} id: {track['id']}")


