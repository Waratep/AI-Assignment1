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

buffer=[]
next_current = []
current = (10,10)
graph={}
graph[current]=set()

next_current.append(current)
limit=2
level=0
while(level<limit):
    print("level:",level," ","limit:",limit)
    for current in next_current:
        print('*current:',current)
        x=current[0]
        y=current[1]
        array = [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
        for i in range (len(array)):
            print('#')
            if checkwall(map1,array[i]):
                if array[i] not in graph:
                    graph[array[i]]=set()
                graph[current].add(array[i])
                buffer.append(array[i])

    next_current=buffer
    print("next_current:", next_current)
#     for keys,values in graph.items():
#         print('keys: ',keys)
#         print('values: ',values)
    level+=1
    print('')
    print('')
