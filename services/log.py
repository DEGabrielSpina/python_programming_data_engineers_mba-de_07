import logging
import os
from dotenv import load_dotenv

class AppLogger:

    _configured = False

    @classmethod
    def get_logger(cls, name: str = "app") -> logging.Logger:
        if not cls._configured:
            load_dotenv()
            logging.basicConfig(
                filename=os.getenv("log_path"),
                filemode="a", 
                level=logging.DEBUG,
                format="%(asctime)s - %(levelname)s - %(message)s"
            )
        return logging.getLogger(name)
    

