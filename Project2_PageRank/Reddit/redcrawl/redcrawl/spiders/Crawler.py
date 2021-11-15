import bs4
import scrapy
from scrapy.utils import response


class RedditSpider(scrapy.Spider):
    name = "reddit"

    start_urls = ["https://www.reddit.com/r/computerscience/"]

    def parse(self, response):
        # List of links on the page
        links = response.css("div::class=_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3").get()

        html = ""
        for link in links:
            url = link.get()

            html += """<a href="{url}" target="_blank">""".format(url=url)
            
            with open("./front.txt" , "a") as page:
                page.write(html)
                page.close()



