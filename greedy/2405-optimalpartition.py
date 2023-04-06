"""
Time: o(n)
Memory: o(26) -> o(1)

"""

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