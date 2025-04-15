from dotenv import load_dotenv
import os
import logging
from typing import List, Dict, Optional

 # configurar logging
logging.basicConfig (
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

def load_env_variables() -> Optional[Dict[str, str]]:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    logging.info("api key cargada correctamente")
    print(f"tu api key {api_key}")

def main():
    vars = load_env_variables()

if __name__ == "__main__":
    main()