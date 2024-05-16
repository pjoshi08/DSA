import collections
from typing import List


# https://leetcode.com/problems/accounts-merge/description/
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = list(range(len(accounts)))

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]  # path compression
                p = par[p]
            return p

        def union(child, parent):
            par[find(child)] = find(parent)

        emailOwner = {}
        # create unions for people having same email, through their index
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in emailOwner:
                    union(i, emailOwner[email])
                emailOwner[email] = i

        ans = collections.defaultdict(list)
        # append emails to correct owner (through their index)
        for email, owner in emailOwner.items():
            ans[find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
