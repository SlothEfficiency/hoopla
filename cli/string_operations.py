from string import punctuation
from nltk.stem import PorterStemmer

def handle_string(input_string: str):
    input_string = to_lower(input_string)
    input_string = rm_punctuation(input_string)

    output = tokenize(input_string)
    output = rm_stopwords(output)

    stemmer = PorterStemmer()
    output = [stemmer.stem(item) for item in output]

    return output

def to_lower(input_string: str) -> str:
    return input_string.lower()

def rm_punctuation(input_string: str) -> str:
    for character in punctuation:
        input_string = input_string.replace(character, "")

    return input_string

def tokenize(input_string: str) -> list:
    return [word for word in input_string.split(" ") if len(word) > 0]


def rm_stopwords(input: list) -> str:
    with open("data/stopwords.txt", "r") as f:
        stopword_string = f.read()

    stopwords = stopword_string.splitlines()

    return [item for item in input if item not in stopwords]
