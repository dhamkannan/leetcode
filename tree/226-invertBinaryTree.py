class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    dummy = TreeNode(left=root)
    def dfs(node):
        if not node:
            return
        temp = node.left
        node.left = node.right
        node.right = temp
        dfs(node.left)
        dfs(node.right)
    dfs(dummy.left)
    return dummy.left