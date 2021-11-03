import json
import requests

#Exercise 2 : Giphy API #1
query = 'hilarous'
level = 'g'
api = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My' 
url = f"https://api.giphy.com/v1/gifs/search?q={query}&rating={level}&api_key={api}"

response = requests.get(url)
# if response.status_code ==200:
    #print(response.json())


gif = response.json()['data']


height_100 = []
for i in range(len(gif)):
    if gif[i]['images']['original']['height']>'100':
        height_100.append(gif[i])

print(len(height_100))

limit = 10
url2 = f"https://api.giphy.com/v1/gifs/search?q={query}&rating={level}&api_key={api}&limit={limit}"

response10 = requests.get(url2)
if response10.status_code ==200:
    gif10 = response10.json()
    #print(gif10)
    print(len(gif10['data']))

# Exercise 3 : Giphy API #2

def give_gif():
    query1 = input('Enter a word ')
    level = 'g'
    api = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My' 
    url3 = f"https://api.giphy.com/v1/gifs/search?q={query1}&rating={level}&api_key={api}"

    url4 ='https://api.giphy.com/v1/gifs/trending?&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
    resp2 = requests.get(url4)
    gif3= resp2.json()

    resp = requests.get(url3)
    if resp.status_code == 200:
        gif2 = resp.json()
        print(len(gif2['data']))
        if len(gif2['data'])==0:
            return gif3
        else:
            return gif2


print(give_gif())

