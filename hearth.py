import requests

source = "print('hello world')"
print(source)

API_RUN_URL = "https://api.hackerearth.com/v3/code/run/"
API_CLIENT_SECRET_KEY = "f8c321f549d832c1be38f82f0a26defc886cd079"

print("making hulalal...")

data = {'client_secret': API_CLIENT_SECRET_KEY, 'source': source,'async': 0, 'lang': "PYTHON"}
# Make the API request here
response = requests.post(API_RUN_URL, data = data).json()

print("end. .end. .end")

#print(response.json())
for key in response:
	if key=="run_status":
		temp = response[key]
		for k in temp:
			print(k," : ",temp[k])
	else:				
		print(key," : ",response[key])
