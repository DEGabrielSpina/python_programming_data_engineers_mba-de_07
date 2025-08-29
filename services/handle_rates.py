import pandas as pd

def handle_rates(df_silver: pd.DataFrame) -> pd.DataFrame:
    
    
    df_silver.sort_values(["coin", "date"], inplace=True)
    
    df_silver['return'] = df_silver.groupby("coin")["rate"].pct_change()
    
    df_silver["volatility"] = df_silver.groupby("coin")["return"].transform("std")
    
    df_silver["date"] = pd.to_datetime(df_silver["date"])
    
    df_silver["date"] = df_silver["date"].dt.date
    
    return df_silver

