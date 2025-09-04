import pandas as pd
import os
from dotenv import load_dotenv

from services.CRUD import CRUD
from services.log import AppLogger

def get_rates() -> pd.DataFrame:

    load_dotenv()
    logger = AppLogger.get_logger("main")

    query_silver = os.getenv("query_silver") 
    
    db: CRUD
    df: pd.DataFrame

    db = CRUD()

    try:
        df = db.select_dataframe(query_silver)
    except Exception as e:
        logger.error(f"Erro ao tentar coletar camada silver no banco {e}")

    return df