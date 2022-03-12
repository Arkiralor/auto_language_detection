LANG_DICT = {
    "am": "Amharic",
    "ar": "Arabic",
    "as": "Assamese",
    "bn": "Bengali",
    "bo": "Tibetan",
    "de": "German",
    "default": "Unknown",
    "en": "English",
    "es": "Spanish",
    "fa": "Persian",
    "fr": "French",
    "gu": "Gujarati",
    "hi": "Hindi",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "lo": "Lao",
    "ml": "Malayalam",
    "mr": "Marathi",
    "ms": "Malay",
    "my": "Burmese",
    "ne": "Nepali",
    "no": "Norweigian",
    "or": "Oriya",
    "pa": "Punjabi",
    "pt": "Portuguese",
    "ru": "Russian",
    "sa": "Sanskrit",
    "sd": "Sindhi",
    "si": "Sinhala",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Tagalog",
    "tr": "Turkish",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-cn": "Chinese"
}

if __name__ == "__main__":
    from datetime import datetime
    from os import sep

    file_name = __file__.split(sep)[-1]
    print(f"[{datetime.now()}]   [{file_name}]  as  [{__name__}]    IMPROPER EXECUTION")
    print(f"[Error]   [{file_name}]    INTENDED FOR IMPORT ONLY")

