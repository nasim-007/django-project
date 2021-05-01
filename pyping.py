# import requests module
import requests
  
# Making a get request
response = requests.get('http://djangoproject2021.herokuapp.com')
  
# print response
print(response)
  
# print url
print(response.url)