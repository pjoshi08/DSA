from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainCount = {}
        for domain in cpdomains:
            i = 0
            while domain[i] != " ":  # capture count
                i += 1
            count = domain[:i]
            full = domain[i + 1:].split(".")
            for i in range(len(full)):
                d = ".".join(full[i:])
                domainCount[d] = int(count) + domainCount.get(d, 0)

        res = []
        for domain, count in domainCount.items():
            res.append(str(count) + " " + domain)

        return res
