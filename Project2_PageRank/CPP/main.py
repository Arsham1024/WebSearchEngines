import csv
from Webnode import Webnode

# Declare a set to hold all the webnodes

# declare a place to store Webnodes Objects
webpages = []


# read list.csv and create Webnode object
with open('Data/list.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    if not webpages:
        # populate the initially empty array
        for line in csv_reader:
            # create a webnode object line by line
            obj = Webnode(line[0], line[1], line[2])
            webpages.append(obj)  # append object to the list
    else:
        # make sure no duplicate webpages
        for webpage in webpages:
            if line[0] != webpage.url:
                for line in csv_reader:
                    # create a webnode object line by line
                    obj = Webnode(line[0], line[1], line[2])
                    webpages.append(obj)  # append object to the list


# dictionary if url, outlinks, and linked by count
url_dict = {}
# perform page rank calculation
counter = 0
# get first page(the comparison page)
for page1 in webpages:
    counter = counter + 1

    match_count = 0
    # loop all pages  in the set to compare against
    for page2 in webpages:

        # compare links see if they link back to first page
        for url in page2.links:
        # compare  page1.url to all page2.links
            if page1.url == url:
                match_count = match_count + 1

    page1.set_numlinkedby(match_count)  # store the numlinked by value in obj
    print(page1.numlinkedby)

