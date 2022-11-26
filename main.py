import requests

api_key = "b7a4b4e8280e4e09b8147fe0ff92ed86"
url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
contents = request.json()

for content in contents['articles']:
    print(content['title'])
