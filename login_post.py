import requests

print("For more advanced login requests with python, Here is great resources:")
print("https://www.scrapingbee.com/blog/how-to-send-post-python-requests/\nhttps://www.geeksforgeeks.org/get-post-requests-using-python/\n\n")
url = input("Enter login url: ")
data = {'username': 'stuedent', 'password': 'Password123'}
r = requests.get(url, data)

print("\nHere is login response: ", r.text)