study-dijkstra
==============

An implementation of Dijkstra's algorithm for learning. Written in Python 3. Done mainly in 2 files - one containing the implementation, and the other containing the test cases (vectors).

dijkstra.py
-----------
This file contains the implementation of the algorithms. Its functions are as follows:

### tester(vector)
The function used to test the implementation using a predefined test vector. The vector can be custom defined, or obtained from the vectors.TV## functions. This is also the starting point to understand how to use other functions.

### dijkstra(graph, start_node, makefull = True)
The function which implements the algorithm. It is modified to store the previous node with the shortest distance (see function 'shortest').
The graph is defined as a dictionary of paths and their cost - in the form:

    (Node1,Node2):length

Node1 and Node2 are end nodes of each path. If the graph is bidirectional, the forward and backward lengths need not be specified separately. Otherwise, specify the lengths separately and set makefull = False. In case of bidirectional graphs, the forward and backward lengths are duplicated for simplifying code.

The result is given out as a searchinfo dictionary of the form:

    Node:(node_in_shortest_path, length)

### shortest(searchinfo, end_node):
The function to find the shortest path to an endpoint, given a searchinfo dictionary from function dijkstra. Output is an ordered list of nodes in the shortest path

###  duplicate_path(in_graph):
A function used internally by function dijkstra. Used to duplicate forward path lengths for backward paths also (eg ('A','B'):5 is duplicated as ('B','A'):5. This reduces the graph description work for bidirectional graphs. To use this option, just leave the 'makefull' argument of 'dijkstra' function as True. Force it to False, otherwise.

vectors.py
----------

This file contains the test cases in the form of functions of name TV## (## is a 2 digit number). Each function returns a tuple that can be fed directly to the dijkstra.tester() function. The tuple contains the inputs and the expected outputs.
