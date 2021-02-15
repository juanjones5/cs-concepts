"""
Example finding connected components:

Given a list accounts, each element accounts[i] is a list of strings, 
where the first element accounts[i][0] is a name, and the rest of the 
elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely 
belong to the same person if there is some email that is common to both 
accounts. Note that even if two accounts have the same name, they may 
belong to different people as people could have the same name. A person 
can have any number of accounts initially, but all of their accounts 
definitely have the same name.

After merging the accounts, return the accounts in the following format: 
the first element of each account is the name, and the rest of the 
elements are emails in sorted order. The accounts themselves can be 
returned in any order.
"""


from collections import defaultdict
from typing import List


class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = DisjointSet(10000)
        email_to_name = {}
        email_to_id = {}
        id_counter = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = id_counter
                    id_counter += 1
                d.union(email_to_id[acc[1]], email_to_id[email])
        ans = defaultdict(list)
        for email in email_to_name:
            ans[d.find(email_to_id[email])].append(email)
        return [[email_to_name[v[0]]] + sorted(v) for v in ans.values()]


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    """
    Single Function Solution
    """
    # 1. Initialize disjoint set
    parent = [i for i in range(10000)]

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        parent[find(i)] = find(j)

    # 2. Build disjoint set
    email_to_name = {}
    email_to_id = {}
    id_counter = 0
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            email_to_name[email] = name
            if email not in email_to_id:
                email_to_id[email] = id_counter
                id_counter += 1
            union(email_to_id[acc[1]], email_to_id[email])

    # 3. Build solution from disjoint set
    filtered_emails = defaultdict(list)
    for email in email_to_name:
        acc_id = find(email_to_id[email])
        filtered_emails[acc_id].append(email)
    result = []
    for email_list in filtered_emails.values():
        result.append([email_to_name[email_list[0]]] + sorted(email_list))
    return result
