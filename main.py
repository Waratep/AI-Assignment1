from Map import getMap , getEmtryMap
from Tree import Node , addData , printLevelsRecursively ,height ,printSingleLevelRecursively
from Maze import checkcanwego , MoveMaze

import time

if __name__ == "__main__":

    x = 10
    y = 10

    lastcurrent = ()
    current = (x,y)
    root = Node(current)
    level = 1

    map = getMap()

    howmany_canwego  = checkcanwego( current , map )
    # print('howmany_canwego',howmany_canwego)
    for cordinate in howmany_canwego:
        if cordinate != None:
            addData(root,cordinate)
    level += 1

    # printLevelsRecursively(root)

    levellist = []
    printSingleLevelRecursively(root,level,levellist)

    current = MoveMaze( current , levellist )
    # print('current',current)
    
    # printLevelsRecursively(root)

###############################################################

    howmany_canwego  = checkcanwego( current , map )
    print('howmany_canwego',howmany_canwego)
    for cordinate in howmany_canwego:
        if cordinate != None:
            addData(root,cordinate)
    level += 1

    printLevelsRecursively(root)

    levellist = []
    printSingleLevelRecursively(root,level,levellist)


    current = MoveMaze( current , levellist )
    print('current',current)
    
    printLevelsRecursively(root)

    for x in current:
        howmany_canwego  = checkcanwego( x , map )
        for cordinate in howmany_canwego:
            if cordinate != None:
                addData(root,cordinate)

        current = MoveMaze( x , levellist )
        print('current',x)

    printLevelsRecursively(root)
    levellist = []
    printSingleLevelRecursively(root,level,levellist)
    current = levellist
    print()
    print('current',current)