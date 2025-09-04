import json
import pandas as pd
import datetime

from services.log import AppLogger

def transfor_consist(response_json: json) -> pd.DataFrame:

    logger = AppLogger.get_logger("main")

    df: pd.DataFrame
    date: datetime.datetime

    date = datetime.datetime.utcfromtimestamp(
                response_json['time_last_update_unix']
            )

    df = pd.DataFrame(response_json['conversion_rates'].items(), columns=['coin', 'rate'])
        
    df['date'] = date

    if df["rate"].isna().any() or (df["rate"] < 0).any():
        logger.warning("Houve linhas que precisaram ser tratadas")
        df= df[df["rate"].ge(0)].dropna()

    return df