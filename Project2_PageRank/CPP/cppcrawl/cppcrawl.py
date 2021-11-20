from typing import Counter
from bs4 import BeautifulSoup
import requests
import csv, os

MAX_PAGES = 500

def collect_links():
    seed = "https://www.cpp.edu/" # seed URL 
    page_num = 1
    all_links = [seed]  # all links under domain of cpp.edu
    counter = 0

    # open csv file to store the links 
    f = open('Project2_PageRank\CPP\cppcrawl\Data\list.csv', 'w', newline='')
    csvFields = ['Page', '# of outlinks', 'outlinks of a page']
    writer = csv.DictWriter(f, fieldnames=csvFields)
    writer.writeheader()

    while page_num <= MAX_PAGES:
        outlink_count = 0 # number of outlinks for each page
        outlinks = []  # to store all outlinks of a certain page
        try:
            html_page = requests.get(all_links[counter]).text  
            soup = BeautifulSoup(html_page, "html.parser")
            body = soup.find('body')

            for link in body.find_all('a', href=True):
                if link['href'].startswith("https://") and ("cpp.edu" in link['href']):
                    all_links.append(link['href'])
                    outlinks.append(link['href'])
                    outlink_count += 1
            
            data_toAdd = {  'Page' : all_links[counter], 
                            '# of outlinks' : outlink_count,
                            'outlinks of a page' : outlinks
                            }
        
            writer.writerow(data_toAdd) # write data to csv file
            
        except Exception:
            pass
        else:
            page_num += 1 # update page number
        finally:
            counter += 1 # update counter
    f.close() # close file

# call the method to collect links
collect_links()