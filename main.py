from Map import getMap , getEmtryMap
from Tree import Node , addData , printLevelsRecursively ,height ,printSingleLevelRecursively
from Maze import checkcanwego 

import time

if __name__ == "__main__":

    x = 10
    y = 10

    lastcurrent = ()
    current = (x,y)
    root = Node(current)
    level = 1

    map = getMap()

    propofmap = 4
    loop = 0
    while (loop < propofmap):

        if (1,1) in current:
            break

        levellist = []
        printSingleLevelRecursively(root,level,levellist)

        current = levellist

        print('current 1',current)
        
        printLevelsRecursively(root)

        for x in current:
            howmany_canwego  = checkcanwego( x , map )
            print('howmany_canwego',howmany_canwego)
            for cordinate in howmany_canwego:
                if cordinate != None:
                    addData(root,cordinate)
                    print('add',cordinate)
            current = levellist
            print('current',x)
        level += 1


        printLevelsRecursively
        levellist = []
        printSingleLevelRecursively(root,level,levellist)
        print('level',level)
        print('levellist',levellist)
        current = levellist
        print()
        print('current 2',current)
        print('============================================================')

        print("#######################################################")
        printLevelsRecursively(root)
        print("#######################################################")

        loop += 1


