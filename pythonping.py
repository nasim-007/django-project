import requests

response = requests.get('https://djangoproject2021.herokuapp.com')


print(response)

print(response.url)