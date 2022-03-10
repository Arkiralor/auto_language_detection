from os import sep
from code.classes import LanguageUtils
from code.constants import DIR_PATH


def generate_text(file_path: str):
    with open(file=file_path, mode='rt', encoding='utf-8')as file:
        data = file.read()

    return data


def check_language(file_name: str = "en_01.txt"):
    text_string = generate_text(DIR_PATH + sep + file_name)
    language_utils = LanguageUtils(text_string)
    lang_detected, confidence_score = language_utils.detect_language()
    print(f"Language detected for '{file_name}' is: {lang_detected}")
    print(f"Confidence in detection: {confidence_score}.")


if __name__ == "__main__":
    check_language()
