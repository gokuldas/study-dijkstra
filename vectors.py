#
# vectors.py
# Dijkstra algorithm project
#
# Copyright (c) 2012, Gokul Das
#

def TV01():
    """Test case from Wikipedia: Dijkstra's algorithm
    http://en.wikipedia.org/wiki/Dijkstra%27s_Algorithm """
    in_graph = {('1','2'):7 , ('1','6'):14, ('1','3'):9 ,\
                ('2','3'):10, ('2','4'):15, ('3','4'):11,\
                ('3','6'):2 , ('4','5'):6 , ('6','5'):9  }
    
    start_node, end_node = '1', '5'
    exp_dist  = {'1':0, '2':7, '3':9, '4':20, '5':20, '6':11}
    exp_path  = ['1', '3', '6', '5']
    return (in_graph, start_node, end_node, exp_dist, exp_path)


def TV02():
    """Test case from youtube: Dijkstra's Algorithm: Shortest Path 
    http://www.youtube.com/watch?v=psg2-6-CEXg """
    in_graph = {('A','B'):2, ('A','C'):9, ('A','G'):4, \
                ('B','C'):4, ('B','D'):2, ('B','F'):7, \
                ('B','G'):6, ('C','D'):3, ('D','E'):5, \
                ('D','F'):3, ('E','F'):3, ('E','H'):4, \
                ('F','G'):5, ('F','H'):4, ('G','I'):2, \
                ('H','I'):3 }

    start_node, end_node = 'A', 'E'
    exp_dist = {'A':(None,0), 'B':('A',2), 'C':('A',9), \
                'D':('B',4) , 'E':('D',9), 'F':('D',7), \
                'G':('A',4) , 'H':('I',9), 'I':('G',6) }
    exp_path = ['A', 'B', 'D', 'E']
    return (in_graph, start_node, end_node, exp_dist, exp_path)
