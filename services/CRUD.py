import pandas as pd
from sqlalchemy import create_engine, text

class CRUD:
    def __init__(self):
        self.conn_url = 'postgresql://neondb_owner:npg_yCjQUFNi84cp@ep-crimson-mud-ads1ann5-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

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