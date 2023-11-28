def diameterOfBinaryTree(root) -> int:
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return 0
        lh = 1 + dfs(node.left)
        rh = 1 + dfs(node.right)
        res = max(res, lh+rh-2)
        return max(lh, rh)
    dfs(root)
    return res