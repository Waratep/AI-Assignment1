from Map import getMap , getEmtryMap
from Tree import Node , addData , printLevelsRecursively ,height ,printSingleLevelRecursively
import time

if __name__ == "__main__":

    x = y = 10
    current = (x,y)

    up = bottom = left = right = None

    root = Node(current)

    howmany_canwego = [0,0,0,0]
    canwego = 0

    map = getMap()

    # up = 0
    if map[x-1][y] != 1: 
        up = (x-1,y)
        addData(root,up)
        howmany_canwego[0] = 1

    # bottom = 1
    if map[x+1][y] != 1: 
        bottom = (x+1,y)
        addData(root,bottom)
        howmany_canwego[1] = 1

    # left = 2
    if map[x][y-1] != 1: 
        left = (x,y-1)
        addData(root,left)
        howmany_canwego[2] = 1

    # right = 3
    if map[x][y+1] != 1: 
        right = (x,y+1)
        addData(root,right)
        howmany_canwego[3] = 1


    counter = 0
    for i in howmany_canwego:
        counter += i

    if (counter == 1):
        for i in range(4):
            if (howmany_canwego[i] == 1):
                canwego = i
                break
        if(canwego == 0): 
            addData(root,up)
            current = up
        if(canwego == 1): 
            addData(root,bottom)
            current = bottom
        if(canwego == 2): 
            addData(root,left)
            current = left
        if(canwego == 3): 
            addData(root,right)
            current = right

    printLevelsRecursively(root)
    print('current',current)

    # if (counter == 2):
    #     for i in range(4):

    #         if (howmany_canwego[i] == 1):
    #             canwego = i
    #             if(canwego == 0): 
    #                 addData(root,up)
    #                 current = up
    #             if(canwego == 1): 
    #                 addData(root,bottom)
    #                 current = bottom
    #             if(canwego == 2): 
    #                 addData(root,left)
    #                 current = left
    #             if(canwego == 3): 
    #                 addData(root,right)
    #                 current = right
        
    # printLevelsRecursively(root)


