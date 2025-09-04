import json
import pandas as pd
from datetime import date

from services.api_exchangerate import get_exchangerate
from services.upload_on_repo import upload_on_repo
from services.upload_silver import upload_silver
from services.upload_gold import upload_gold
from services.get_rates import get_rates
from services.handle_rates import handle_rates
from services.transfor_consist import transfor_consist
from services.log import AppLogger

if __name__ == '__main__':

    response_json: json
    df: pd.DataFrame

    logger = AppLogger.get_logger("main")
  
    str_date = date.today().strftime("%Y-%m-%d")

    # Pega dados na api
    response_json = get_exchangerate()

    # Salva json em repository na camada raw
    upload_on_repo(response_json)

    # Tratamentos para camada silver
    df = transfor_consist(response_json)

    # Salva na camada silver
    upload_silver(df)

    # Pega dados salvos na camada silver
    df_silver = get_rates()

    # Inclui retorno e volatilidade transformando assim em ouro
    df_gold = handle_rates(df_silver)

    # Pega só as datas do dia
    df_gold = df_gold[df_gold["date"] == pd.to_datetime(str_date).date()]

    # Salva em camada ouro
    upload_gold(df_gold)

    logger.info("Executado com sucesso.")
    




    
    
    
    

    



    
