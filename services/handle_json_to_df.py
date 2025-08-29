import json
import pandas as pd
import datetime

def handle_json_to_df(response_json: json) -> pd.DataFrame:

    df: pd.DataFrame
    date: datetime.datetime

    date = datetime.datetime.utcfromtimestamp(
                response_json['time_last_update_unix']
            )

    df = pd.DataFrame(response_json['conversion_rates'].items(), columns=['coin', 'rate'])
        
    df['date'] = date

    return df