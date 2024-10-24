import requests

url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"

querystring = {"id":"UxxajLWwzqY"}

headers = {
	"X-RapidAPI-Key": "-",
	"X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()

#response filtering
title= response['title'] #title
lengthSeconds = response['lengthSeconds'] #duration in seconds
thumbnail_temp = response['thumbnail'][1]
thumbnail= thumbnail_temp['url'] #url of thumbnail
formats = response['formats'] #video quality list
adaptiveFormats = response['adaptiveFormats'] #all other qualities including audio

#printing data
print("Title: ",title)
print("Duration:", lengthSeconds)
print(thumbnail)

print('\n\n\n')

for i in formats:
    print('qualityLabel: ',i['qualityLabel'])
    print('url: ',i['url'])

print('\n\n\n')

for i in adaptiveFormats:
    try:
        print('qualityLabel: ',i['qualityLabel'])
        print("formate:",i['mimeType'])
        print('size:',int(i['contentLength'])*10**(-6))
        print('url: ',i['url'])
    except:
        print('audioQuality: ',i['audioQuality'])
        print("formate:",i['mimeType'])
        print('size:',int(i['contentLength'])*10**(-6))
        print('url: ',i['url'])