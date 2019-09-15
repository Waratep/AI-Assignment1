def checkcanwego(_current,_map):

    x = _current[0]
    y = _current[1]

    howmany_canwego = []
    up = bottom = left = right = None

    map = _map

    # up = 0
    if map[x-1][y] != 1: 
        up = (x-1,y)
        # return up

    # bottom = 1
    if map[x+1][y] != 1: 
        bottom = (x+1,y)
        # return left

    # left = 2
    if map[x][y-1] != 1: 
        left = (x,y-1)
        # return left

    # right = 3
    if map[x][y+1] != 1: 
        right = (x,y+1)
        # return right

    howmany_canwego.append(up)
    howmany_canwego.append(bottom)
    howmany_canwego.append(left)
    howmany_canwego.append(right)
        

    return howmany_canwego 

     