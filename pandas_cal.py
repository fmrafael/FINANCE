from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import random
import requests


r = Request('https://br.investing.com/economic-calendar/', headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(r).read()
soup = BeautifulSoup(response, "html.parser")
table = soup.find_all(class_ = "js-event-item")
    
result = []
r_time=[]
r_evento=[]
r_currency=[]
r_intensity=[]
    
for bl in table:
               
  time_d = bl.find(class_ ="first left time js-time").text
  evento = bl.find(class_ ="left event").text.strip()
  currency = bl.find(class_ ="left flagCur noWrap").text
  intensity = bl.find(class_="left textNum sentiment noWrap").get('title')

  r_time.append(time_d)
  r_evento.append(evento)
  r_currency.append(currency)
  r_intensity.append(intensity)

df = pd.DataFrame(list(zip(r_time,r_evento,r_currency,r_intensity)),columns=['horario','evento','currency','intensity'])

#print(r_intensity)

pd.set_option('display.max_rows', 500)

 
currency_list = ['USD','BRL','EUR']
vol_list = ['Volatilid. Esperada Alta','Volatilid. Esperada Moderada']
#vol = 


f_df = df[ (df['intensity'].str.strip().isin(vol_list) & (df['currency'].str.strip().isin(currency_list) ) )]

df_styled = f_df[['horario','currency','evento']]


#weather
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring_rain = {"q":"São Paulo","days":"1"}

headers_rain = {
    'x-rapidapi-key': "C4e4A0veUwpEi3lQDOLNgWYX59sUBN86",
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }

response_rain = requests.request("GET", url, headers=headers_rain, params=querystring_rain).json()


max_temp_sp = response_rain['forecast']['forecastday'][0]['day']['maxtemp_c']
min_temp_sp = response_rain['forecast']['forecastday'][0]['day']['mintemp_c']
rain = response_rain['forecast']['forecastday'][0]['day']['daily_chance_of_rain']



API_KEY_FX = os.environ['API_KEY_FX']

#FX_closing

url_fx = f'https://fcsapi.com/api-v3/forex/latest?id=1799&access_key={API_KEY_FX}'

r_fx = requests.request("GET",url_fx)

data_fx = r_fx.json()['response']
data_f = ", ".join([data['c'] for data in data_fx])


#quote_day
r_q = requests.get("https://quotes.rest/qod?category=inspire&language=en")

response = r_q.json()

author = response['contents']['quotes'][0]['quote'][0]

quote = response['contents']['quotes'][0]['quote'] 
author = response['contents']['quotes'][0]['author'] 

quote_day = f"{quote} {author}"




welcome_msg = f'Mínima/Máxima temperatura em SP: {min_temp_sp}- {max_temp_sp} °C, probabilidade de chuva: {rain}%. Dolar fechou cotado ontem a {data_f}.' '  ' + random.choice(["Bom dia, bons negócios!","Segue a agenda de eventos mais relevantes para o dia de BRL, USD e EUR",quote_day, "Agenda Econômica para o dia"])







 
  

    


     

         
   

    



#print(json.dumps(news, indent=2))