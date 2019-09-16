from Map import getMap
import time

def checkwall(map,current):
    x = current[0]
    y = current[1]
    if(map[x][y] != 1):
        return True
    return False

def bi_directional_search(graph, start, goal):
    # Check if start and goal are equal.
    if start == goal:

        return [start]
    # Get dictionary of currently active vertices with their corresponding paths.
    active_vertices_path_dict = {start: [start], goal: [goal]}
    # Vertices we have already examined.
    inactive_vertices = set()

    while len(active_vertices_path_dict) > 0:
        
        # Make a copy of active vertices so we can modify the original dictionary as we go.
        # print(active_vertices_path_dict.keys())
        active_vertices = list(active_vertices_path_dict.keys())
        for vertex in active_vertices:
            # Get the path to where we are.
            current_path = active_vertices_path_dict[vertex]
            # print('Current path : ', current_path)
            # print(current_path)
            # Record whether we started at start or goal.
            origin = current_path[0]
            # Check for new neighbours.
            current_neighbours = set(graph[vertex]) - inactive_vertices
            # print('Neightbor : ', current_neighbours)
            # Check if our neighbours hit an active vertex
            if len(current_neighbours.intersection(active_vertices)) > 0:
                for meeting_vertex in current_neighbours.intersection(active_vertices):
                    # Check the two paths didn't start at same place. If not, then we've got a path from start to goal.
                    if origin != active_vertices_path_dict[meeting_vertex][0]:
                        # Reverse one of the paths.
                        active_vertices_path_dict[meeting_vertex].reverse()
                        # return the combined results
                        return print(active_vertices_path_dict[vertex] + active_vertices_path_dict[meeting_vertex])

            # No hits, so check for new neighbours to extend our paths.
            if len(set(current_neighbours) - inactive_vertices - set(active_vertices))  == 0:
                # If none, then remove the current path and record the endpoint as inactive.
                active_vertices_path_dict.pop(vertex, None)    
                inactive_vertices.add(vertex)
            else:
                # Otherwise extend the paths, remove the previous one and update the inactive vertices.
                for neighbour_vertex in current_neighbours - inactive_vertices - set(active_vertices):
                    active_vertices_path_dict[neighbour_vertex] = current_path + [neighbour_vertex]
                    active_vertices.append(neighbour_vertex)
                active_vertices_path_dict.pop(vertex, None)
                inactive_vertices.add(vertex)
    return None
    
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


num = 0
success = False

while(num < 20):
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
    num += 1

seconds = time.time()
bi_directional_search(graph, (10,10), (1,1))
print('used time',time.time() - seconds , 'seconds')
