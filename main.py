import requests
from sending_email import send_mail
from mail_pass import api, urls


api_key = api

url = urls

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