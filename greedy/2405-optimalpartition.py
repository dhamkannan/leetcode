s = "abacaba"
def partitionString(s):
    res = 1
    cache = set()
    for c in s:
        if c in cache:
            res += 1
            cache = set()
        cache.add(c)
    return res
print(partitionString(s))