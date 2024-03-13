import requests
#from track_recommender import recommender


def send_simple_message(responseData, email):
    
	# Correctly formatted for loop inside an f-string
	text_value = "\n".join([responseData['tracks'][i]['name'] for i in range(5)])

	# Now use the text_value in the requests.post call
	response = requests.post(
		"https://api.mailgun.net/v3/sandboxf8ba72ab16fb480cac65b530fbd0df92.mailgun.org/messages",
		auth=("api", "d3b61a1d0913592c82812e22b053db35-b02bcf9f-3dd025b1"),  # Replace 'your-api-key' with your actual Mailgun API key
		data={
			"from": "mailgun@sandboxf8ba72ab16fb480cac65b530fbd0df92.mailgun.org",
			"to": email,
			"subject": "Music",
			"text": text_value
		}
	)
	return response
if __name__ == "__main__":
    print(send_simple_message())