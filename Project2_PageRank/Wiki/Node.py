class Node:
    # init the node class for every single page on the list.
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.pagerank = 1
