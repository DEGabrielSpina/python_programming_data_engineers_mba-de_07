import json
import os
from datetime import datetime
from dotenv import load_dotenv

from services.log import AppLogger


def upload_on_repo(fl_json: json) -> None:

    load_dotenv()
    logger = AppLogger.get_logger("main")

    dir_raw_path = os.getenv("dir_raw_path")

    str_date = datetime.today().strftime("%Y%m%d")
 
    try:
        with open(f'{dir_raw_path}/cotacoes{str_date}.json', 'w', encoding='utf-8') as f:
            json.dump(fl_json, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Erro ao gravar json na camada raw {e}")