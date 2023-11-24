import requests

url = "https://shazam-api6.p.rapidapi.com/shazam/recognize/"

audio_url= "https://drive.usercontent.google.com/download?id=1ut3JXQo_E0KUTogsu9UVI1ZuTY3gLUt4&export=download&authuser=0&confirm=t&uuid=d20fa040-8735-4ea3-a3e0-7968d2c1b0ef&at=APZUnTWWonJx242QBP7zkwYGk2_E:1700848894524" #audio url

querystring = {"url":f"{audio_url}"}

headers = {
	"X-RapidAPI-Key": "035f085157msh229319bf92d56f3p122af5jsn241c25adf036",
	"X-RapidAPI-Host": "shazam-api6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())