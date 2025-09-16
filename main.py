import requests
from sending_email import send_mail

api_key = "6a143001bc014e79a0775016fef5c0dd"

url = "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=6a143001bc014e79a0775016fef5c0dd"

# Make request
request = requests.get(url)

#get dictionary with data
content = request.json()

#Access the articles title and description
body = ""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] +  2*"\n"

body = body.encode("utf-8")
send_mail(massage=body)