import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import re
import random
import time
import csv
from langdetect import detect

# Stating URLs
all_seeds = ["https://en.wikipedia.org/wiki/Main_Page",
             "https://fa.wikipedia.org/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C",
             "https://es.wikipedia.org/wiki/Espa%C3%B1a"]

# Max number of pages crawling
# change this later to 3000
MAX_Pages = 500

# This is a global variable indicating the current language that is being checked.
# default is english
all_langs = ["english" , "farsi" , "spanish"]
current_lang = all_langs[0]
# This will give the correct seed for the current language and set it to current seed
current_seed = all_seeds[all_langs.index(current_lang)]

# Creating report.csv file for links and number outlinks
header = ['Link', 'Outlinks']
with open('report.csv', 'w', encoding='UTF8', newline='') as report:
    writer = csv.writer(report)
    writer.writerow(header)
    report.close()

# crawler function
def crawler():
    # getting the starter HTML and turning it into plain text
    # text_page = requests.get(seed).text
    # To increment with each pages successfully crawled
    links_tocrawl = []
    current_seed = all_seeds[0]
    # This method is the engine of the crawler and while loop is located here
    # By the end of each crawl cycle a language is fully crawled.
    for i in range(len(all_langs)):
        print(current_seed)
        pages_visited = 0
        # To store all the links to crawl
        # initially only has the seed at index 0
        links_tocrawl = [current_seed]
        crawl(MAX_Pages, links_tocrawl, pages_visited)

        current_seed = all_seeds[i+1]

    # Outputting how many links have been recorded.
    print("The number of pages visited : ", len(links_tocrawl))

    # store files in repository
    for i, link in enumerate(links_tocrawl):
        text_page = requests.get(link).text
        # call to extract files
        extract_file(text_page, i + 1)
        # stop iteration after maximum page limit
        if i >= MAX_Pages:
            break


# While loop of the crawler, This is separated because
# the crawler needs to run multiple times and with different specifications
def crawl(MAX_Pages, links_tocrawl, pages_visited):
    # Temporary while loop timer for debugging
    start1 = time.time()

    # These conditions should limit the amount of pages visited to maximum we want
    while pages_visited < MAX_Pages and len(links_tocrawl) < MAX_Pages:
        # Starting timer for politeness time-out
        start_time = time.time()
        text_page = requests.get(links_tocrawl[pages_visited]).text
        crawl_delay = time.time() - start_time

        # Extract all the links in the page to be searched over later.
        extract_links(links_tocrawl, text_page, pages_visited)

        # Need to put "Done" in the array links_tocrawl once a page's extraction is complete

        # End of each iteration add one to counter
        pages_visited += 1

        # Time-out based on time it takes to load the page and randomly multiplied by 1 or 2
        time.sleep(random.uniform(1, 2) * crawl_delay)

    # Prints runtime of while loop
    end = time.time()
    print("Runtime : ", end - start1)

# This method extract (save) the html file associated with a link
def extract_file(text_page, page):
    soup = BeautifulSoup(text_page, 'html.parser')
    # use the page title to name each file (some titles are undefined)
    # title = soup.find('title').text
    # title = re.sub(r"\W+|_", " ", title)

    # create/open a new file in repository and save the content
    with open(f'./Project1_Crawler/repository/English/file{page}.txt', 'w', encoding='utf-8') as theFile:
        theFile.write(soup.prettify())

# This method will extract only URLs and save them to the links to crawl array.
def extract_links(links_tocrawl, text_page, pages_visited):
    # Counter for number ouf outlinks found in a link
    outlinks = 0

    # This will take out all the links on a page and store the in the links_tocrawl array to be crawled.
    for link in BeautifulSoup(text_page, parse_only=SoupStrainer('a'), features="html.parser"):
        # This will do 3 checks
        #  1. checks if the link has href attribute (because these are links)
        #  2. checks to see if these hrefs start with http so that we know these are URLs and not relative links
        #  3. detects a language of a page in advance of being store in the to crawl array.
        if link.has_attr('href') \
                and link['href'].startswith("http"):  # \
            # and detect_url_language(link['href']) == current_lang:
            links_tocrawl.append(link['href'])
            outlinks += 1
        # else should skip this iteration of the loop and continue
        else:
            continue

    # Print out result and write link and outlinks to report.csv
    print("Current Link:", links_tocrawl[pages_visited], "Number of Outlinks:", outlinks)
    report_row = [links_tocrawl[pages_visited], outlinks]
    with open('report.csv', 'a', encoding='UTF8', newline='') as report:
        writer = csv.writer(report)
        writer.writerow(report_row)

    # Print out the result
    print("This is the array content : ", links_tocrawl)
    print("")

# Method for identifying the language of a URL on the fly
def detect_url_language(url):
    # Text version of HTML
    text = requests.get(url).text
    # Parse the text with beautiful soup
    soup = BeautifulSoup(text, 'html.parser')
    # This section will check the website's language by checking the header first then checking the body
    try:
        lang = soup.html['lang']
    except:
        print("couldn't detect language of the webiste, so skipped it.")
        return None

    if lang == 'en':
        return "english"
    if lang == 'fa':
        return "farsi"
    if lang == 'es':
        return "spanish"
    else:
        return None


if __name__ == "__main__":
    crawler()