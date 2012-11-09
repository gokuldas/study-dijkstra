
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
    exp_path = ['A', 'B', 'D', 'E']
    return (in_graph, start_node, end_node, exp_dist, exp_path)
