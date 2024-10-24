import requests

url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/"

querystring = {"url":"https://www.instagram.com/reel/Cz-0JHrpU_O/?igshid=MzY1NDJmNzMyNQ=="} #video link

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()[0] #only url(nothing else)

print('url:',response)