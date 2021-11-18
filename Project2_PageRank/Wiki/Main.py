
# This function does one iteration of the page rank algorithm
# graph is the matrix of all the nodes
# l is the lambda typically set to 0.15 or 0.2
def pagerank_iter(graph , l):
    # put all the nodes in a list
    node_list = graph.nodes
    # for each node in this list update its page rank
    for node in node_list:
        # call the page rank function with lambda = 0.15 and number of nodes in the graph
        node.update_rank(len(graph.nodes) , l)

# This function just updates the page rank of one node. gets called directly on the node
# takes n = number of nodes in the graph
# lambda with default value of 0.15
def update_rank(self, n, l = 0.15):
  # get all the nodes that point to this node
  neighbors = self.parents
  # The sigma portion of the equation
  pagerank_sum = sum((node.pagerank / len(node.children)) for node in neighbors)
  # in corporate the lambda randomness to avoid loops and holes
  random_walk = l / n
  # assign the final pagerank to the node.
  self.pagerank = random_walk + (1-l) * pagerank_sum