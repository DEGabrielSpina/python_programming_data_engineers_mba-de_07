import pandas as pd
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

class CRUD:
    def __init__(self):

        load_dotenv()
        self.conn_url = os.getenv("conn_url")
        

    def insert_dataframe(self, df: pd.DataFrame, table_: str, schema_: str) -> None:

        engine = create_engine(self.conn_url)
    
        df.to_sql(
            name=table_,
            con=engine, 
            schema=schema_, 
            if_exists="append", 
            index=False, 
            method="multi"
        )

    def select_dataframe(self, query: str) -> pd.DataFrame:

        engine = create_engine(self.conn_url)

        df = pd.read_sql(
            sql=query,
            con=engine
        )

        return df
    
    def execute(self, query: str) -> None:

        engine = create_engine(self.conn_url)

        with engine.begin() as conn:
            conn.execute(text(query))