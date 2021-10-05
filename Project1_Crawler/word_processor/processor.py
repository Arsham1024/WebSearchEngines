# Purpose: Apply Zipf's Law and Heap's Law to web crawled data
# Accepts English, Spanish, and lastly Farsi(non-latin script)

import os

# Graphing for Zipf's + Heap's Law
import pandas as pd
import matplotlib.pyplot as plt

# Language Processing
from bs4 import BeautifulSoup, SoupStrainer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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
def import_text_as_string(text_path):
    string = "text"
    for filename in os.listdir(text_path):
        with open(os.path.join(text_path, filename), 'r') as file:
            file_text = file.readlines()
            string = string + ' '.join(file_text) # Append file content to list
    return string


# Seperate words into list
def tokenize(text_list):
    re.split('\W+', text_list)
    tokens = re.split('\W+', text_list)
    return tokens


# remove stop words
def remove_stopwords(text, stoplist):
    text_no_stops = [word for word in text if word not in stoplist]
    return text_no_stops


def html_text_only(string):
    soup = BeautifulSoup(string, 'html.parser')
    text_only = soup.get_text()
    return text_only

# Calls previous methods, accepts languages like "english", "spanish", "farsi"
# expects path "../repository/English/"
def process_text(language, path):
    stopwords = load_stopwords(language)  # Load Stopwords
    text = import_text_as_string(path)  # Import crawled text
    soup = BeautifulSoup(text, 'html.parser')  # soup object
    text = soup.get_text()  # get only text (REMOVE HTML...)
    text = text.lower()
    text = tokenize(text)  # Create list of each word
    text = remove_stopwords(text, stopwords)  # remove stopwords

    # Produce a Dictionary {word, word count}
    text = list(itertools.chain(text))
    text = Counter(text)

    return text


english = process_text("english", "../repository/English/")
print(english)

spanish = process_text("spanish", "../repository/Spanish/")
print(spanish)

farsi = process_text("farsi", "../repository/Farsi/")
print(farsi)

