from services.CRUD import CRUD

import pandas as pd
from datetime import datetime, date


def upload_df_to_db(df: pd.DataFrame, schema: str, table: str):
    
    db = CRUD()

    date = df['date'].iloc[0]

    db.execute(f"DELETE FROM {schema}.{table} where date = '{date}'")
    
    db.insert_dataframe(
        df,
        table,
        schema
    )