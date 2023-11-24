import requests

url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/"

querystring = {"url":"https://www.instagram.com/reel/Cz-0JHrpU_O/?igshid=MzY1NDJmNzMyNQ=="} #video link

headers = {
	"X-RapidAPI-Key": "035f085157msh229319bf92d56f3p122af5jsn241c25adf036",
	"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()[0] #only url(nothing else)

print('url:',response)