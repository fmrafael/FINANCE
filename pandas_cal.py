from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import random
from quote import *

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

welcome_msg = quote_day

#random.choice(["Bom dia, bons negócios!","Segue a agenda de eventos mais relevantes para o dia de BRL, USD e EUR","Bom dia!!",])






 
  

    


     

         
   

    



#print(json.dumps(news, indent=2))