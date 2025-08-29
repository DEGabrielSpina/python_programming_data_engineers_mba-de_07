import json
from datetime import datetime

def upload_on_repo(fl_json: json) -> None:


    str_date = datetime.today().strftime("%Y%m%d")
 

    with open(f'C:/Users/gabri/OneDrive/Desktop/python_programming_data_engineers_mba-de_07/files/cotacoes{str_date}.json', 'w', encoding='utf-8') as f:
        json.dump(fl_json, f, indent=2, ensure_ascii=False)