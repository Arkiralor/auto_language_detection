# Automatic Language Detection via Spacy

<p> A Module to automatically detect the language of a unicode text. </p>

## Setup:

``` bash
1. python -m venv env
2. source env/bin/activate
3. python -m pip install --upgrade pip
1. python -m pip install -requirements.txt
```

## Usage:

1. Save the text as a ```.txt``` file in the directory name ```text_samples```.

2. Run the command: ```python main.py <file_name.txt>``` where ```file_name.txt``` is ___only___ the name of the file, not the path.

## Notes:

1. Currently, this script is only using the _medium_ ```EN``` model for language detection. It can detect languages via the UTF-8 characters used. As soon as a general-purpose model is found that can accurately work on multiple languages simultaneously, it will be used instead.

2. Documentation for the model can be found on the official [Spacy Model Documentation Page.](https://spacy.io/models) 