       # 0 1 2 3 4 5 6 7 8 9 10 11
map1 = [[1,1,1,1,1,1,1,1,1,1,1,1], # 0
        [1,0,0,0,0,0,1,0,0,0,0,1], # 1
        [1,0,1,0,1,0,1,1,1,0,1,1], # 2
        [1,0,1,0,1,0,0,0,0,0,0,1], # 3
        [1,0,0,1,1,1,0,1,0,1,1,1], # 4
        [1,0,1,1,0,1,1,1,0,1,0,1], # 5
        [1,0,0,0,0,1,0,1,0,1,0,1], # 6
        [1,1,1,1,0,1,0,1,0,1,0,1], # 7
        [1,0,0,0,0,0,0,1,0,1,0,1], # 8
        [1,1,0,1,1,1,0,1,0,0,0,1], # 9
        [1,0,0,0,0,0,0,0,0,1,0,1], # 10
        [1,1,1,1,1,1,1,1,1,1,1,1]] # 11

def checkwall(map1,current):
    x=current[0]
    y=current[1]
    if(map1[x][y] != 1):
        return True
    return False

def dfs_paths(graph, start, goal):
    
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
                
            else:
                stack.append((next, path + [next]))

buffer=[]
next_current = []
current = (10,10)
graph={}
graph[current]=set()

next_current.append(current)
limit = 20
level = 0
start = (10,10)
end = (1,1)
while(level<limit):
#     print("level:",level," ","limit:",limit)
    if list(dfs_paths(graph, start, end)) != [] : 
        print('fined path from start to end')
        print(list(dfs_paths(graph, start, end)))
        break
    for current in next_current:
#         print('*current:',current)
        x=current[0]
        y=current[1]
        array = [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
        for i in range (len(array)):            
            if checkwall(map1,array[i]):
                if array[i] not in graph:
                    graph[array[i]]=set()
                graph[current].add(array[i])
                buffer.append(array[i])

    next_current = buffer
    buffer = []
#     print("next_current:", next_current)
#     print("graph:",graph)
#     for keys,values in graph.items():
#         print('keys: ',keys)
#         print('values: ',values)
    level += 1
#     print('')
#     print('')
print('level',level)

import numpy as np
import matplotlib.pyplot as plt

def printMap(map1):
    # fig, ax = plt.subplots()
    min_val, max_val = 0, 12
    for i in range(12):
        for j in range(12):
            c = map1[i][j]
    #         ax.text(i+0.5, j+0.5, str(c), va='center', ha='center')
    plt.figure()
    plt.matshow(map1, cmap=plt.cm.Blues)
    # ax.set_xlim(min_val, max_val)
    # ax.set_ylim(min_val, max_val)
    # ax.set_xticks(np.arange(max_val))
    # ax.set_yticks(np.arange(max_val))
    # ax.grid()

printMap(map1)