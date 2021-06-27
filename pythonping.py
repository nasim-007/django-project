import requests

response = requests.get('https://google.com')


print(response)

print(response.url)