
class Node:
    def __init__(self, data,left = None ,right = None,forward = None,bottom=None):
        self.data = data
        self.left = left
        self.right = right
        self.forward = forward
        self.bottom = bottom
        
def addData(r,data):
    if r is None:
        return Node(data)
    else:
        
        if r.data != data:
            if data[0] < r.data[0] :
                r.forward = addData(r.forward,data)             
            elif data[1] < r.data[1]:
                r.left = addData(r.left,data) 
            elif data[1] > r.data[1]:
                r.right = addData(r.right,data) 
            else:
                r.bottom = addData(r.bottom,data)       
        return r
            
def printLevelsRecursively(root) :
        h = height(root);
        for i in range (h):
            print("Level ",i+1," : ",end=' ')
            printSingleLevelRecursively(root, i+1)
            print('')


def height(r):
    if r is None :
        return 0
    return max(height(r.left),height(r.forward),height(r.right))+1

def printSingleLevelRecursively(root,level):
    if root == None:
        return;
    if level == 1:
        print(root.data,end=' ')
    else:
        printSingleLevelRecursively(root.left, level - 1)        
        printSingleLevelRecursively(root.right, level - 1)
        printSingleLevelRecursively(root.forward, level - 1)
        printSingleLevelRecursively(root.bottom, level - 1)


