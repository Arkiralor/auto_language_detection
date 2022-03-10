'''
Python program to automatically detect the Natural Language of a given text-document.
'''

from code.functions import check_language

if __name__ == "__main__":
    file_name: str = "sa_01.txt"
    check_language(file_name=file_name)
