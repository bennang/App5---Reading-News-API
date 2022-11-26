import requests
from send_email import send_email

user_email = "benjaminazj@gmail.com"

api_key = "b7a4b4e8280e4e09b8147fe0ff92ed86"
url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
contents = request.json()

body = ""
for content in contents['articles']:
    if content['title'] is not None:
        body = body + content['title'] + '\n' + content['description'] + 2*'\n'

message = f"""Subject: News Letter

{body}
"""

message = message.encode("utf-8")
send_email(message)
