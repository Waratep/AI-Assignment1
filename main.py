from Map import getMap
import time

def checkwall(map,current):
    x = current[0]
    y = current[1]
    if(map[x][y] != 1):
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

if __name__ == "__main__":

    map = getMap()

_buffer = []
next_current = []
current = (10,10)
graph = {}
graph[current] = set()

next_current.append(current)
limit = 20
level = 0
start = (10,10)
end = (1,1)

seconds = time.time()

while(level < limit):

    if list(dfs_paths(graph, start, end)) != [] : 
        print('fined path from start to end')
        print(list(dfs_paths(graph, start, end)))
        print('used time',time.time() - seconds , 'seconds') 
        break
    for current in next_current:
        x = current[0]
        y = current[1]
        array = [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
        for i in range (len(array)):            
            if checkwall(map,array[i]):
                if array[i] not in graph:
                    graph[array[i]] = set()
                graph[current].add(array[i])
                _buffer.append(array[i])

    next_current = _buffer
    _buffer = []
    level += 1
