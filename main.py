import requests
import os
from pandas_cal import *
from datetime import datetime



url = 'https://api.linkedin.com/v2/ugcPosts'


access_token = os.environ['access_token']


urn = os.environ['urn']


author = f"urn:li:person:{urn}"



headers = {'X-Restli-Protocol-Version': '2.0.0',
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'}



publication = df_styled.to_string(index=False)

def post_link():
  api_url = url

  body = {
      "author": author,
      "lifecycleState": "PUBLISHED",
      "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": publication
                },
                "shareMediaCategory": "NONE"
            },
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTIONS"
        },
    }

  response = requests.post(api_url,headers=headers,json=body)

  if response.status_code == 201:
        print("Success")
        print(response.content)
  else:
        print(response.content)

post_link()


