
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

def compare_BST(root1,root2):

    if root1 == None and  root2 == None:
        return True

    if root1!= None and root2 != None:
        return (root1.data == root2.data and compare_BST(root1.left,root2.left) and compare_BST(root1.right,root2.right))

    return False

if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7,8]
    arr2 = [1,2,3,4,5,6,7,8]

    root1 = myBST(arr1)
    root2 = myBST(arr2)

    isIt = compare_BST(root1,root2)
    print(isIt)

    arr1 = [1,2,3,4,5,6,7,8]
    arr2 = [1,2,3,4,5,6,7,8,9]

    root1 = myBST(arr1)
    root2 = myBST(arr2)

    isIt = compare_BST(root1,root2)
    print(isIt)
