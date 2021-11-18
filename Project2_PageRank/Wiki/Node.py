class Node:
    # init the node class for every single page on the list.
    def __init__(self, name):
        self.name = name
        # All the nodes/pages that point to this page
        self.parents = []
        # all the pages that this page points to
        self.children = []
        self.pagerank = 1
