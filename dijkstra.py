def duplicate_path(in_graph):
    """Update graph with reverse path costs"""
    out_graph = {(i[1],i[0]):in_graph[i] for i in in_graph.keys()}
    out_graph.update(in_graph)
    return out_graph


def dijkstra(graph, start_node, makefull = True):
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
    si = dijkstra(in_graph, start_node)
    spath = shortest(si, end_node)
    s = _output.format(in_graph, start_node, end_node, \
                       si, exp_dist, \
                       spath, exp_path)
    print(s)
    

