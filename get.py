import requests

url = input("Enter url: ")
r = requests.get(url)
print("\nGET response: ", r.text)