
import requests

url = "https://spotify23.p.rapidapi.com/search/"
def searchMusic(song):


    querystring = {"q": song ,"type":"tracks","offset":"2","limit":"2","numberOfTopResults":"5"}

    headers = {
        "X-RapidAPI-Key": "0e566a50abmshcbb2f7203fd11b5p14de52jsn691d435af501",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    id = data['tracks']['items'][0]['data']['id']
    print(f"id: {id}")
    return id


# if __name__ == "__main__":
#     searchMusic()












