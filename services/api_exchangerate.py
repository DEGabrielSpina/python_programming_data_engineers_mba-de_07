import requests
import json
import os
from dotenv import load_dotenv

from services.log import AppLogger

def get_exchangerate() -> json:

    load_dotenv()
    logger = AppLogger.get_logger("main")

    url = os.getenv("url")
    api_key = os.getenv("api_key")

    headers = {
        "Authorization": f"Bearer {api_key}",  
    }

   
    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        return response.json()
    else:
        logger.error("Erro ao acessar a api exchange:", response.status_code, response.text)
        raise Exception("Erro:", response.status_code, response.text)


    