# Several methods used to Open a Raw cralwed data file and
# Cleans data by removing unwanted language features and words

import os
# Language Processing
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import re
# Used for Counting the words
from collections import Counter
import itertools


# Load Stored Language Stopwords
def load_stopwords(lang):
    # Add Local Path to Files, Remove Install Dependency of NLTK
    nltk.data.path.append("./nltk_data")
    lang.lower()
    # Define the Languages
    stops = []
    if (lang == 'english'):
        stops = stopwords.words('english')
    elif (lang == 'spanish'):
        stops = stopwords.words('spanish')
    elif (lang == 'farsi'):
        stops = stopwords.words('farsi')
    else:
        stops = []
    return stops


# Import ALL text from repository directory into a simple string
# path example "../repository/English"
def import_text_as_string(text_path: str):
    string = "text"
    for filename in os.listdir(text_path):
        with open(os.path.join(text_path, filename), 'r') as file:
            file_text = file.readlines()
            string = string + ' '.join(file_text)  # Append file content list
    return string


# Seperate words into list
def tokenize(text: str):
    re.split('\W+', text)
    tokens = re.split('\W+', text)
    return tokens


# remove stop words
def remove_stopwords(text: str, stoplist: list):
    text_no_stops = [word for word in text if word not in stoplist]
    return text_no_stops


# Remove Punctuation
def remove_punct(text: str):
    text_no_punct = [word for word in text if word.isalpha()]
    return text_no_punct


# Remove any single character
def remove_single_letters(text: str):
    # There is probably a better way to do this??
    single = ["a", "b", "c", "d", "e", "f", "g",
              "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]
    text_no_single = [word for word in text if word not in single]
    return text_no_single


# Return only Text, NO HTML
def html_text_only(text: str):
    soup = BeautifulSoup(text, 'html.parser')
    text_only = soup.get_text()
    return text_only


# Catch all for any other words we should perhaps remove...
def remove_non_words(text: str):
    non_words = ["url", "https", "www", "com",
                 "org", "http"]
    text_cleaned = [word for word in text if word not in non_words]
    return text_cleaned


# Calls previous methods, accepts languages like "english", "spanish", "farsi"
# expects path "../repository/English/"
# PIPELINE to Clean text
def process_text(language, path):
    stopwords = load_stopwords(language)  # Load Stopwords
    text = import_text_as_string(path)  # Import crawled text
    text = html_text_only(text)
    text = text.lower()
    text = tokenize(text)  # Create list of each word
    text = remove_stopwords(text, stopwords)  # remove stopwords
    text = remove_non_words(text)
    text = remove_punct(text)  # remove non alphabet values
    text = remove_single_letters(text)
    # Produce a Dictionary {word, word count}
    text = list(itertools.chain(text))
    text = Counter(text)
    return text
