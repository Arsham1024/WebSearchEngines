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


# Code sanity check section 
import_text("../repository/English")


# Import ALL text from Resository into a list
def import_text(text_path):
    text_repo_en = "../repository/English"
    counter = 0

    text_list = []
    for filename in os.listdir(text_repo_en):
        with open(os.path.join(text_repo_en, filename), 'r') as file:
            file_text = file.readlines()
            text_list.append(file_text)


# Text, remove NON-Words for processing 
#def clean_text(list_of_text):


# Tokenize Text and produce Graphical Data
