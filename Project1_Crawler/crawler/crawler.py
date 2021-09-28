import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request

# Stating URL
seed = "https://www.apple.com/"

# HTML Parser
parser = HTMLParser

# Max number of pages crawiling
# change this later to 3000
pages = 1000

# crawler function
def crawler(MAX_Pages):
    # getting the starter HTML and turning it into plain text
    # text_page = requests.get(seed).text
    # To increment with each pages successfully crawled
    pages_visited = 0
    # To store all the links to crawl
    # initially only has the seed at index 0
    links_tocrawl = [seed]

    # This function takes an array to save all the links extracted and an html page in text format (not URL!)


    # Need a breadth first search type of algorithm for this crawler
    # These conditions should limit the amount of pages visited to maximum we want
    while pages_visited < MAX_Pages and len(links_tocrawl) < MAX_Pages:
        text_page = requests.get(links_tocrawl[pages_visited]).text
        extract_links(links_tocrawl, text_page)

        # Need to put "Done" in the array links_tocrawl once a page's extraction is complete


        # End of each iteration add one to counter
        pages_visited += 1
    

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


if __name__ == "__main__":
    crawler(pages)
