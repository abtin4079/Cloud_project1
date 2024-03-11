import requests
from track_recommender import recommender


def send_simple_message():
	
    responseData = recommender()
    
    return requests.post(
		"https://api.mailgun.net/v3/sandboxf8ba72ab16fb480cac65b530fbd0df92.mailgun.org/messages",
		auth=("api", "d3b61a1d0913592c82812e22b053db35-b02bcf9f-3dd025b1"),
		data={"from": "mailgun@sandboxf8ba72ab16fb480cac65b530fbd0df92.mailgun.org",
			"to": "abtin.aptitude@gmail.com",
			"subject": "Music",
			"text": f"{responseData['tracks'][2]['name']}"})

if __name__ == "__main__":
    print(send_simple_message())