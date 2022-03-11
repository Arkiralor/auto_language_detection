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
        if len(input_args) == 2:
            file_path = input_args[1]
            check_language(file_path)
            logging.info(f"[{datetime.now()}]   [{__file__}|{__name__}] [TARGET: {file_path}]   SUCCESS ")
        else:
            logging.info(f"[{datetime.now()}]   [{__file__}|{__name__}] Target filename not provided")
    except Exception as e:
        logging.info(f"[{datetime.now()}]   Error in [{__file__}|{__name__}]: {e}")

if __name__ == "__main__":
    main()
