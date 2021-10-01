import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import re
from langdetect import detect


# Stating URL
seed = "https://en.wikipedia.org/wiki/Main_Page"

# HTML Parser
parser = HTMLParser

# Max number of pages crawiling
# change this later to 3000
pages = 500

# This is a global variable indicating the current language that is being checked.
# default is english
current_lang = "english"

# crawler function
def crawler(MAX_Pages):
    # getting the starter HTML and turning it into plain text
    # text_page = requests.get(seed).text
    # To increment with each pages successfully crawled
    pages_visited = 0
    # To store all the links to crawl
    # initially only has the seed at index 0
    links_tocrawl = [seed]

    # These conditions should limit the amount of pages visited to maximum we want
    while pages_visited < MAX_Pages and len(links_tocrawl) < MAX_Pages:
        text_page = requests.get(links_tocrawl[pages_visited]).text

        # if the language is not english skip this page
        if not detect_language(text_page)== current_lang:
            continue

        # Extract all the links in the page to be searched over later.
        extract_links(links_tocrawl, text_page)

        # Need to put "Done" in the array links_tocrawl once a page's extraction is complete
        # End of each iteration add one to counter
        pages_visited += 1

    # Outputing how many links have been recorded.
    print("The number of pages visited so far : ", len(links_tocrawl))

    # store files in repository
    for i,link in enumerate(links_tocrawl):
        text_page = requests.get(link).text
        # call to extract files
        extract_file(text_page, i+1) 
        # stop iteration after maximum page limit
        if i >= pages: 
            break


# This method extract (save) the html file associated with a link
def extract_file(text_page, page):
    soup = BeautifulSoup(text_page,'html.parser')
    # use the page title to name each file (some titles are undefined)
    # title = soup.find('title').text
    # title = re.sub(r"\W+|_", " ", title) 
        
    # create/open a new file in repository and save the content 
    with open(f'./Project1_Crawler/repository/English/file{page}.txt', 'w', encoding='utf-8') as theFile:
        theFile.write(soup.prettify()) 

# This method will extract only URLs and save them to the links to crawl array.
def extract_links(links_tocrawl, text_page):
    # For handling exeptions
    successful = True
    # This will take out all the links on a page and store the in the links_tocrawl array to be crawled.
    for link in BeautifulSoup(text_page, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href') and not link['href'].startswith("/") and not link['href'].startswith("#"):
            links_tocrawl.append(link['href'])
    # Print out the result
    print("This is the array content right now: " , links_tocrawl)
def detect_language(text_page):
    if detect(text_page) == 'en':
        return "english"
    if detect(text_page) == 'fa':
        return "farsi"
    if detect(text_page) == 'es':
        return "spanish"


if __name__ == "__main__":
    crawler(pages)
