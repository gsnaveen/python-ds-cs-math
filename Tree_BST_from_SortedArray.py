# Creating a BST from a sorted Array [1,2,3,4,5,6,7,8] and print it 

class Node ():

    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def myBST(arr):

    if not arr:
        return None

    middle = len(arr)//2
    root = Node(arr[middle])

    root.left = myBST(arr[:middle])
    root.right = myBST(arr[middle+1:])

    return root


def printBST(root,what):

    if not root:
        return

    print(what, root.data)
    printBST(root.left,str(root.data) + "<--" +"left")
    printBST(root.right,str(root.data) + "-->" "right")

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    root = myBST(arr)
    printBST(root,"root")
