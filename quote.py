import requests

r = requests.get("https://quotes.rest/qod?category=inspire&language=en")

response = r.json()

 

author = response['contents']['quotes'][0]['quote'][0]

quote = response['contents']['quotes'][0]['quote'] 
author = response['contents']['quotes'][0]['author'] 

quote_day = f"{quote} {author}"

 

  



#print(response2)