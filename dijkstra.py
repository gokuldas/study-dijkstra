def duplicate_path(in_graph):
    """Update graph with reverse path costs"""
    out_graph = {(i[1],i[0]):in_graph[i] for i in in_graph.keys()}
    out_graph.update(in_graph)
    return out_graph


def dijkstra(graph, start_node, end_node, makefull = True):
    """Implementation of Dijkstra's algorithm"""
    if makefull: graph = duplicate_path(graph) 
    # uvnodes : unvisited nodes
    uvnodes = {i[0] for i in graph.keys()}
    # dictionary in the form node : (nearest_node, min_dist)
    searchinfo = {i:(None, float('inf')) for i in uvnodes}
    searchinfo[start_node] = (None, 0)

    while True:
        minm, current = float('inf'), None
        for node in uvnodes:
            cand = searchinfo[node][1]
            if cand < minm:
                current, minm = node, cand
        if minm == float('inf'): break

        uvnodes.remove(current)
        for node in uvnodes:
            path = (current, node)
            if path in graph:
                tentv = searchinfo[current][1] + graph[path]
                if tentv < searchinfo[node][1]:
                    searchinfo[node] = (current, tentv)

    return searchinfo
      

def shortest(searchinfo, end_node):
    """Find the shortest path from search result of dijkstra fn"""
    path, current = [end_node], end_node
    while searchinfo[current][0] != None:
        current = searchinfo[current][0]
        path.append(current)
    path.reverse()
    return path


_output = """\
Input graph is         : {0}\n
Start node: {1}\n   
End node  : {2}\n

Search distances are   : {3}\n
Expected distances are : {4}\n

Shortest path is       : {5}\n
Expected path is       : {6} 
"""

def tester(vector):
    """Test function: use TVxx() function to get test vector"""
    in_graph, start_node, end_node, exp_dist, exp_path = vector
    si = dijkstra(in_graph, start_node, end_node)
    spath = shortest(si, end_node)
    s = _output.format(in_graph, start_node, end_node, \
                       si, exp_dist, \
                       spath, exp_path)
    print(s)
    
    

def TV01():
    in_graph = {('1','2'):7 , ('1','6'):14, ('1','3'):9 ,\
                ('2','3'):10, ('2','4'):15, ('3','4'):11,\
                ('3','6'):2 , ('4','5'):6 , ('6','5'):9  }
    
    start_node, end_node = '1', '5'
    exp_dist  = {'1':0, '2':7, '3':9, '4':20, '5':20, '6':11}
    exp_path  = ['1', '3', '6', '5']
    return (in_graph, start_node, end_node, exp_dist, exp_path)


def TV02():
    in_graph = {('A','B'):2, ('A','C'):9, ('A','G'):4, \
                ('B','C'):4, ('B','D'):2, ('B','F'):7, \
                ('B','G'):6, ('C','D'):3, ('D','E'):5, \
                ('D','F'):3, ('E','F'):3, ('E','H'):4, \
                ('F','G'):5, ('F','H'):4, ('G','I'):2, \
                ('H','I'):3 }

    start_node, end_node = 'A', 'E'
    exp_dist = dict()
    exp_path = dict()
    return (in_graph, start_node, end_node, exp_dist, exp_path)
    
