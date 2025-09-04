import os
from dotenv import load_dotenv
from google import genai

from services.CRUD import CRUD
from services.log import AppLogger


def ask(question, csv):

    load_dotenv()
    logger = AppLogger.get_logger("main")

    google_api_key = os.getenv("google_api_key")
    

    prompt = f'''
    Você é um analista financeiro. Responda em português.

    Pergunta: {question}

    Use SOMENTE os dados a seguir (em CSV):
    {csv}
    '''

    client = genai.Client(api_key=google_api_key)

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    ) 

    logger.info(f'Pergunta: {question} \nRetorno gemini: {resp.text}')
    return resp.text

if __name__ == '__main__':

    load_dotenv()

    query_data = os.getenv("query_data")

    db = CRUD()

    df = db.select_dataframe(query_data)

    csv = df.to_csv(index=False)

    while True:
        question = input("Digite seu pergunta:\n")
        
        if question == 'exit':
            break
        else:
            print(ask(question, csv))