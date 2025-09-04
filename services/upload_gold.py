import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

from services.CRUD import CRUD
from services.log import AppLogger

def upload_gold(df: pd.DataFrame):

    load_dotenv()
    logger = AppLogger.get_logger("main")

    schema = os.getenv("schema") 
    table_gold = os.getenv("table_gold")
    dir_gold_path = os.getenv("dir_gold_path")

    date = df['date'].iloc[0]
    str_date = date.strftime("%Y-%m-%d")

    # Subindo no banco
    db = CRUD()

    try:
        db.execute(f"DELETE FROM {schema}.{table_gold} where date = '{str_date}'")
        
        db.insert_dataframe(
            df,
            table_gold,
            schema
        )
    except Exception as e:
        logger.error(f"Erro ao tentar salvar camada gold no banco {e}")

    # Subindo no repo
    try:
        df.to_parquet(path=f'{dir_gold_path}/cotacoes{str_date}.parquet')
    except Exception as e:
        logger.error(f"Erro ao tentar salvar camada gold no repo {e}")

