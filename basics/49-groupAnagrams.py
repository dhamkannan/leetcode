from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]


def groupAnagrams():
    res =  defaultdict(list)
    for str in strs:
        count = [0] * 26
        for s in str:
            count[ord(s) - ord('a')] += 1
        res[tuple(count)].append(str)
    return res.values()
print(groupAnagrams())