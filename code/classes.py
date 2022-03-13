from code.choices import LANG_DICT
from logger.logger import logging
from datetime import datetime
from time import time, sleep


import spacy
from spacy_langdetect import LanguageDetector
from spacy.language import Language as ln
from spacy_langdetect import LanguageDetector
import en_core_web_sm


class LanguageUtils:
    '''
    Class to handle language detection in text:
    '''
    _input_text:str = None
    _threshold:float = 0.95

    def __init__(self, input_text: str):
        '''
        Initialization method for the class:
        '''
        self._input_text = input_text
        logging.info(f"[{datetime.now()}]   [{__name__}] INITIALISED")

    def __repr__(self):
        '''
        Representation method for the class:
        '''
        return f"{self._input_text}"

    def detect_language(self):
        '''
        Method to detect the language of the passed text:
        '''
        try:
            ## 001 (prithoo): MAJOR CHANGE in Spacy v3:
            ## Language.factory() no longer accepts a class directly as the first arg.
            ## Instead, now it calls a tagged decorator that calls a function that return the class-pointer.
            ln.factory("language_detector", func=create_lang_detector)

            ## 001 (prithoo): Loading the NLP model to the nlp object
            nlp = en_core_web_sm.load(disable=[None])
            logging.info(f"[{datetime.now()}]   [{__name__}] MODEL LOADED [{nlp.__dict__['_meta']['name']}]")


            ## 001 (prithoo): Max length of the input text.
            nlp.max_length = 2_000_000

            nlp.add_pipe("language_detector", last=True)

            ## 001 (prithoo): Initial parsing of the text by the nlp object
            doc = nlp(self._input_text)
            logging.info(f"[{datetime.now()}]   [{__name__}] INPUT TEXT PARSED")

            lang_code = doc._.language.get("language")
            confidence_score = doc._.language.get("score")

            logging.info(f"[{datetime.now()}]   [{__name__}] INFO : {doc._.language}")

            if confidence_score >= self._threshold and lang_code in LANG_DICT.keys():
                return LANG_DICT.get(lang_code), confidence_score
            else:
                lang_code = "default"
                logging.info(f"[{datetime.now()}]   [{__name__}]  WARNING: SCORE TOO LOW [{confidence_score}]")
                return LANG_DICT.get(lang_code), confidence_score
                
        except Exception as ex:
            logging.info(f"[{datetime.now()}]   Error in [{__name__}]: {ex}")


@ln.factory('language_detector')
def create_lang_detector(nlp, name):
    '''
    function to create language model.
    '''
    return LanguageDetector()


if __name__ == "__main__":
    pass
