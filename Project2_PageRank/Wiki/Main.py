import Node
# This function does one iteration of the page rank algorithm
# graph is the matrix of all the nodes
# l is the lambda typically set to 0.15 or 0.2
def pagerank_iter(allnodes , l):
    # put all the nodes in a list
    node_list = allnodes
    # for each node in this list update its page rank
    for node in node_list:
        # call the page rank function with lambda = 0.15 and number of nodes in the graph
        node.update_rank(len(node_list) , l)



# This function just updates the page rank of one node. gets called directly on the node
# takes n = number of nodes in the graph
# lambda with default value of 0.15
def update_rank(self, n, l = 0.15):
  # get all the nodes that point to this node
  neighbors = self.parents

  # The sigma portion of the equation
  # for all the nodes in the neighbors of this particular node make sigma function
  # put all these sums into the sigma
  sigma = sum((node.pagerank / len(node.children)) for node in neighbors)

  # in corporate the lambda randomness to avoid loops and holes
  # This is random suuf way discussed in class at the end.
  random_surf = l / n

  # assign the final pagerank to the node.
  self.pagerank = random_surf + (1-l) * sigma



# populate the graph with all the nodes


def main():
    

    # a matrix of all the nodes connected
    node1 = Node(self , 1)
    node2 = Node(self , 2)

    # Need an initialize page rank to each 1/n

    node1.pagerank = 1/2
    node1.parents.append(node2)
    node1.children.append(node2)

    node2.pagerank = 1/2
    node2.parents.append(node1)
    node1.children.append(node1)

    graph = [node1, node2]
    # lambda value
    l = 0.15

    # iterate 10 times
    for i in range(1):
        # call the function to iterate through and update
        pagerank_iter(graph, l)


    print(node.pagerank for node in graph)

