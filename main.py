'''
Python program to automatically detect the Natural Language of a given text-document.
'''
import sys
from code.functions import check_language

def main():
    input_args = sys.argv
    try:
        if len(input_args) == 2:
            file_path = input_args[1]
            check_language(file_path)
        else:
            print("Please provide a file path as an argument.")
    except Exception as e:
        print(f"Error in {__name__}: {e}")

if __name__ == "__main__":
    main()
