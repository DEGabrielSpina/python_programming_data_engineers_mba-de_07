from google import genai

from services.CRUD import CRUD


def ask(question, csv):

    prompt = f'''
    Você é um analista financeiro. Responda em português.

    Pergunta: {question}

    Use SOMENTE os dados a seguir (em CSV):
    {csv}
    '''

    client = genai.Client(api_key='AIzaSyCafZupwAfXKzSQfdkgqDUfLWw041mopnQ')

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    ) 

    return resp.text

if __name__ == '__main__':

    db = CRUD()

    df = db.select_dataframe('select * from py_for_de.coin_rate_return_vol')

    csv = df.to_csv(index=False)

    while True:
        question = input("Digite seu pergunta:\n")
        
        if question == 'exit':
            break
        else:
            print(ask(question, csv))

    



'''
client = genai.Client(api_key='AIzaSyCafZupwAfXKzSQfdkgqDUfLWw041mopnQ')

resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
) 
'''