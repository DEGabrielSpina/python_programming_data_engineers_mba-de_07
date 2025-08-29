import requests
import json

def get_exchangerate() -> json:

    url = "https://v6.exchangerate-api.com/v6/6510a68a39473c708cee5cf4/latest/BRL"
    api_key = "6510a68a39473c708cee5cf4"

    headers = {
        "Authorization": f"Bearer {api_key}",  
    }

   
    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Erro:", response.status_code, response.text)


    