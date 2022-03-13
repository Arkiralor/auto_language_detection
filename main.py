'''
Python program to automatically detect the Natural Language of a given text-document.
'''
import sys
from code.functions import check_language
from logger.logger import logging
from datetime import datetime

def main():
    input_args = sys.argv
    try:
        logging.info(f"[{datetime.now()}]   [{__name__}] INITIALISING ")
        if len(input_args) >= 2:
            file_path = input_args[-1]
            check_language(file_path)
            logging.info(f"[{datetime.now()}]   [{__name__}] [TARGET: {file_path}]   SUCCESS ")
        else:
            logging.info(f"[{datetime.now()}]   ERROR   in  [{__name__}] Target FILENAME not provided")
    except Exception as e:
        logging.info(f"[{datetime.now()}]   ERROR in [{__name__}]: {e}")

if __name__ == "__main__":
    main()
