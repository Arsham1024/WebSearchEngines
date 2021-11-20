import csv
from Node import Node
import requests
from bs4 import BeautifulSoup

################### Global variables
baseURL = "https://en.wikipedia.org"
URLs_tocrawl = []
# For only wikipedia pages
wikis = []

# to put all the node items made.
nodes = []

################### Helpers
def append(url):
    return baseURL+url

# This function filters wikipedia pages and formats them to get ready for request method
def format_href():
    global item, current
    # This loop will grab each href and filter only for those that are wikipedia websites and formats them correctly
    for item in href:
        # make item a str object so we can do operations
        current = str(item)
        if 'wiki' in current and current.startswith("http"):
            wikis.append(current)
        elif 'wiki' in current and current.startswith("/"):
            wikis.append(append(current))


# Open the file and read in all the urls to crawl and make the partial URLs a complete address
with open("./Output/list.csv", "r") as f:
    reader = csv.reader(f, delimiter=',')
    
    temp = []
    # making the URLs full addresses
    for row in reader:
        temp.append(baseURL+row[1])
    # Limiting the amount of links to crawl because it was out of hand!
    # you can delete this for loop and see, make proper adjustments
    for i in range(30):
        URLs_tocrawl.append(temp[i])


################### Main part
# make an array with 30 nodes
# for incrimenting
count = 0
for i in range(len(URLs_tocrawl)):
    nodes.append(Node(f"{URLs_tocrawl[i]}"))
    count += 1

for i in nodes:
    print(i.name)

# For every single URL that was crawled from wikipedia directory
# make a node associated with and
# put all the children (aka all the links that are in the page) in it.
i = 0
for item in URLs_tocrawl:
    # Use bs4 to parse the html
    current = requests.get(item).text
    soup = BeautifulSoup(current, "lxml")

    # get all a tags
    all_a_tags = soup.findAll('a')
    href =  []

    # Get hrefs
    for item in all_a_tags:
        # edit a tags for only hrefs / urls so we can request later
        href.append(item.get('href'))

    # Format the href to match the desired url and get rid of none wikipedias
    format_href()




print(wikis , "\n" , len(wikis))
print(len(URLs_tocrawl))
