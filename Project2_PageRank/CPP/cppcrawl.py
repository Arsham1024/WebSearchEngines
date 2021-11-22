from typing import Counter
from bs4 import BeautifulSoup
import requests
import csv, os

MAX_PAGES = 500

def collect_links():
    seed = "https://www.cpp.edu/" # seed URL
    page_num = 1 # count pages
    all_links = [seed]  # all links under domain of cpp.edu
    counter = 0  

    # open csv file to store the links
    f = open('Data\list.csv', 'w', newline='')

    # column names - pages, number of outlinks from that page, list of outgoing links
    csvFields = ['Link', 'Count', 'Outlink']
    writer = csv.DictWriter(f, fieldnames=csvFields)
    writer.writeheader()

    while page_num <= MAX_PAGES:
        outlink_count = 0 # number of outlinks for each page
        outlinks = []  # to store all outlinks of a certain page
        try:
            # send request to a page and parsed its url to get html content
            html_page = requests.get(all_links[counter]).text  
            soup = BeautifulSoup(html_page, "html.parser")
            body = soup.find('body')

            # iterate over all links in html body and fetch the urls under the domain, cpp.edu
            for link in body.find_all('a', href=True):
                if link['href'].startswith("https://") and ("cpp.edu" in link['href']):
                    all_links.append(link['href']) # add each link to the list of all_links
                    outlinks.append(link['href']) # add it to list of outgoing urls of a page
                    outlink_count += 1

            # write row cotent as dictionary and add each entry to the csv file
            data_toAdd = {  'Link' : all_links[counter],
                            'Count' : outlink_count,
                            'Outlink' : outlinks
                            }
            writer.writerow(data_toAdd) 

        except Exception: 
            pass # continue iteration if page does not contain any url
        else:
            page_num += 1 # increment page 
        finally:
            counter += 1 # increment counter
    f.close() # close file

# call the method to collect links
collect_links()
