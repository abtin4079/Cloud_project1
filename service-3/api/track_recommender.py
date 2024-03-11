import requests
from serach import searchMusic



url = "https://spotify23.p.rapidapi.com/recommendations/"

def recommender():
    id = searchMusic()
    querystring = {"limit":"5","seed_tracks":f"{id}"}

    headers = {
        "X-RapidAPI-Key": "0e566a50abmshcbb2f7203fd11b5p14de52jsn691d435af501",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    responseData = response.json()
    for i in range(5):
        print(responseData['tracks'][i]['name'])

    return responseData
