from typing import List


# https://leetcode.com/problems/search-suggestions-system/description/
class Solution:
    # 99%
    def suggestedProducts3(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == c]
            res.append(products[:3])
        return res

    # Beats 66%, better solution
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        patterns = {}
        for i in range(1, len(searchWord) + 1):
            search = searchWord[:i]
            patterns[search] = []
        for product in products:
            for i in range(1, len(product) + 1):
                prd = product[:i]
                if prd in patterns:
                    if len(patterns[prd]) < 3:
                        patterns[prd].append(product)
                else:
                    break
        res = []
        for val in patterns.values():
            res.append(val)
        return res

    # Accepted Solution but slow
    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        for i in range(1, len(searchWord) + 1):
            search = searchWord[:i]
            res.append([])
            for prod in products:
                if prod.startswith(search):
                    res[-1].append(prod)
                if len(res[-1]) == 3: break
        return res


obj = Solution()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
# products = ["havana"]
searchWord = "mouse"
# searchWord = "tatiana"
print(obj.suggestedProducts(products, searchWord))
