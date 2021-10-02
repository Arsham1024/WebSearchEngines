# Purpose: Apply Zipf's Law and Heap's Law to web crawled data
# Accepts English, Spanish, and lastly Farsi(non-latin script)

import os

# Graphing for Zipf's + Heap's Law
import pandas as pd

# Language Processing
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re


# Load Stored Language Stopwords
def load_stopwords(lang):
    # Add Local Path to Files, Remove Install Dependency of NLTK
    nltk.path.append("./nltk_data")
    lang.str.lower()

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


# Import ALL text from repository directory into a list
def import_text(text_path):

    text_list = []
    for filename in os.listdir(text_path):
        with open(os.path.join(text_path, filename), 'r') as file:
            file_text = file.readlines()
            text_list.append(file_text) # Append file content to list

    return text_list

def tokenize(text_list):
    re.split('\W+', text_list)
    tokens = re.split('\W+', text_list)
    return tokens
