import requests


def shazamApi(attachment):
    url = "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"

   # attachment = open("F:/UNIVERCITY/term8/cloud computing/homework/HW1/9923020_HW1/13_-_him_i_-_g-eazy_halsey_320.mp3", 'rb')




    files = { "upload_file": attachment}
    headers = {
        "X-RapidAPI-Key": "0e566a50abmshcbb2f7203fd11b5p14de52jsn691d435af501",
        "X-RapidAPI-Host": "shazam-api-free.p.rapidapi.com"
    }

    response = requests.post(url, files=files, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"the song name is : {data['track']['title']}")
        return data['track']['title']
    else:
        print(f"Shazam Error: {response.status_code}")
        
if __name__ == "__main__":
    shazamApi()