# Webnode which defines the url, total outlinks, and the list of outlinks
class Webnode:
    def __init__(self, url, numoutlinks, outlinks):
        self.url = url
        self.numoutlinks = numoutlinks

        # take data comma list as s a python list
        clean_links = outlinks.replace("[", "")
        clean_links = clean_links.replace("]", "")
        clean_links = clean_links.replace("'", "")
        clean_split_links = clean_links.split(",")
        self.links = clean_split_links

        self.numlinkedby = 0

    def set_numlinkedby(self, value):
        self.numlinkedby = value
