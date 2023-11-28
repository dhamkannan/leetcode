
def maxDepth(root) -> int:        
    def dfs(node):
        if not node:
            return 0
        lh = 1+ dfs(node.left)
        rh = 1 + dfs(node.right)
        return max(lh, rh)
    return dfs(root)