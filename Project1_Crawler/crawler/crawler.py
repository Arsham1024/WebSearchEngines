import requests
from html.parser import HTMLParser

# Stating URL
seed = "https://www.apple.com/"

# HTML Parser
parser = HTMLParser

# Max number of pages crawiling
# change this later to 3000
pages = 10

# crawler function
def crawler(MAX_Pages):
    # getting the starter HTML and turning it into plain text
    start_page = requests.get(seed).text
    # To increment with each pages successfully crawled
    pages_visited = 0
    # To store all the links to crawl
    links_tocrawl = []

    # Need a breadth first search type of algorithm for this crawler
    # These conditions should limit the amount of pages visited to maximum we want
    while pages_visited < MAX_Pages and len(links_tocrawl) < MAX_Pages:
        data = parser.feed(start_page)
        tag




if __name__ == "__main__":
    crawler(pages)
