"""
Time: 
Memory: 
"""

from collections import defaultdict
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

def accountsMerge(accounts):

    par = [i for i in range(len(accounts))]
    rank = [1 for i in range(len(accounts))]

    def union(node1, node2):
        p1, p2 = find(node1), find(node2)
        if p1 == p2:
            return
        elif rank[p1] > rank[p2]:
            par[node2] = p1
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[node1] = p2
            par[p1] = p2
            rank[p2] += rank[p1]

    def find(node):
        while node != par[node]:
            par[node] = par[par[node]]
            node = par[node]
        return node

    emailMap = {}
    for i, account in enumerate(accounts):
        for j in range(1, len(account)):
            email = account[j]
            if email in emailMap:
                union(i, emailMap[email])
            else:
                emailMap[email] = i
    
    emailGroups = defaultdict(list)
    for email, i in emailMap.items():
        parent = find(i)
        emailGroups[parent].append(email)

    res = []
    for i, emails in emailGroups.items():
        res.append([accounts[i][0]] + sorted(emails))

    return res


print(accountsMerge(accounts))