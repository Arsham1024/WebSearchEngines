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

from collections import Counter
import itertools
import urllib.request

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



#def import_text_as_list(text_path):
#
#    text_list = []
#    for filename in os.listdir(text_path):
#        with open(os.path.join(text_path, filename), 'r') as file:
#            file_text = file.readlines()
#            text_list.append(file_text) # Append file content to list
#
#    return text_list

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


# example code section Waiting on full dataset from processor team
en_sw = load_stopwords("english")
#text_with_html = import_text_as_string("../repository/English/")
#text_only = html_text_only(text_with_html)


url = "https://webflow.com/blog/the-web-design-process-in-7-simple-steps"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
text = text.lower()
text = tokenize(text)
text = remove_stopwords(text, en_sw)

counted_text = list(itertools.chain(text))
counted_text = Counter(counted_text)
print(counted_text)

