# -------------------------------------------------------------------------------------
# Trees
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def inorder_traverse(root):
    if root:
        inorder_traverse(root.left)
        print(root.val, end=" ")
        inorder_traverse(root.right)
        
def preorder_traverse(root):
    if root:
        print(root.val, end=" ")
        preorder_traverse(root.left)
        preorder_traverse(root.right)
        
def postorder_traverse(root):
    if root:
        postorder_traverse(root.left)
        postorder_traverse(root.right)
        print(root.val, end=" ")
        
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal: ",inorder_traverse(root))
print("Preorder traversal: ",preorder_traverse(root))
print("Postorder traversal: ",postorder_traverse(root))