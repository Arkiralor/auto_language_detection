'''
Script to sort the LANGUAGE DICTIONARY by the keys and to generate a new 
"choices.py" file to store the python dictionary to be used for import.
'''

from code.choices import LANG_DICT
import json

FILE_PATH = "code\choices_2.py"
DICT_NAME = "LANG_DICT = " ## This is the name of the output dictionary that will be written to the .py file.

lang_dict = sorted(LANG_DICT)
LANG_DICT_2 = {}

for key in lang_dict:
    LANG_DICT_2[key]=LANG_DICT.get(key)

if_name_block = '''
\nif __name__ == "__main__":
    pass
'''
op_string = DICT_NAME + json.dumps(LANG_DICT_2, indent=4) + if_name_block

with open(FILE_PATH, 'w+t', encoding='utf-8') as op_file:
    op_file.write(op_string)



