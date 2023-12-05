# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, curSum):
            nonlocal targetSum
            if not node:
                return False
            curSum += node.val
            if not node.left and not node.right:
                return targetSum == curSum
            return dfs(node.left, curSum) or dfs(node.right, curSum)
        return dfs(root, 0)