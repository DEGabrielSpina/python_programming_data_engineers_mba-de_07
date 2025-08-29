import json
import pandas as pd
from datetime import date

from services.api_exchangerate import get_exchangerate
from services.handle_json_to_df import handle_json_to_df
from services.upload_on_repo import upload_on_repo
from services.upload_df_to_db import upload_df_to_db
from services.get_rates import get_rates
from services.handle_rates import handle_rates

if __name__ == '__main__':

    response_json: json
    df: pd.DataFrame
  
    str_date = date.today().strftime("%Y-%m-%d")

    # Pega dados na api
    response_json = get_exchangerate()

    # Salva json em repository
    upload_on_repo(response_json)
   
    # Transforma em um dataframe
    df = handle_json_to_df(response_json)

    # Salva no banco camada prata
    upload_df_to_db(df, 'py_for_de', 'coin_rate')

    # busca dados do banco para fazer o tratamento da camada ouro
    df_silver = get_rates()

    # Acrecenta colunas de retorno e volatilidade
    df_gold = handle_rates(df_silver)

    # Pega só as datas do dia
    df_gold = df_gold[df_gold["date"] == pd.to_datetime(str_date).date()]

    # Salva no banco camada ouro
    upload_df_to_db(df_gold, 'py_for_de', 'coin_rate_return_vol')

    print('Done!')




    
    
    
    

    



    
