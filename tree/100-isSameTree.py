def isSameTree(self, p, q) -> bool:
    if not p and not q:
        return True
    elif not p or not q or p.val != q.val:
        return False
    return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))