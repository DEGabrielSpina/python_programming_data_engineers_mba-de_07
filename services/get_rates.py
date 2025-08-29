import pandas as pd

from services.CRUD import CRUD

def get_rates() -> pd.DataFrame:
    
    db: CRUD
    df: pd.DataFrame

    db = CRUD()

    df = db.select_dataframe('SELECT * from py_for_de.coin_rate')

    return df