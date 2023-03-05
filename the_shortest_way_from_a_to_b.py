import math
graph = {
    '1' : [['2',3],['4',4],['3',2]],
    '2' : [['1',3]],
    '3' : [['1',2],['4',1],['5',3]],
    '4' : [['1',4],['3',1],['8',3],['6',4]],
    '5' : [['3',3],['6',7]],
    '6' : [['5',7],['4',4],['7',5],['9',2]],
    '8' : [['4',3],['7',1],['10',2]],
    '7' : [['8',1],['6',5]],
    '9' : [['6',2],['10',1]],
    '10' : [['8',2],['9',1]]
}
def mota(graph,start,what_find,weight,was):
    the_best_node = math.inf
    if start == what_find:
        if weight < the_best_node:
            the_best_node = weight
            return the_best_node
    saw = was[:]
    saw.append(start)
    for i in graph[start]:
            if not i[0] in was:
                a = mota(graph,i[0],what_find,weight+i[1],saw)
                if a < the_best_node:
                    the_best_node = a
    return the_best_node

for i,j in graph.items():
    print(f'from 1 to {i} is',mota(graph,'1',i,0,[]))
