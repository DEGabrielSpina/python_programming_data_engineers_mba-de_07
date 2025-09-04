import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

from services.CRUD import CRUD
from services.log import AppLogger


def upload_silver(df: pd.DataFrame):

    load_dotenv()
    logger = AppLogger.get_logger("main")

    schema = os.getenv("schema") 
    table_silver = os.getenv("table_silver")
    dir_silver_path = os.getenv("dir_silver_path")

    date = df['date'].iloc[0]
    str_date = date.strftime("%Y-%m-%d")

    # Subindo no banco
    db = CRUD()

    try:

        db.execute(f"DELETE FROM {schema}.{table_silver} where date = '{str_date}'")
        
        db.insert_dataframe(
            df,
            table_silver,
            schema
        )
    except Exception as e:
        logger.error(f"Erro ao tentar salvar camada silver no banco {e}")

    try:
        # Subindo no repo
        df.to_parquet(path=f'{dir_silver_path}/cotacoes{str_date}.parquet')
    except Exception as e:
        logger.error(f"Erro ao tentar salvar camada silver no repo {e}")

