from collections import defaultdict, deque
from typing import List


class Solution:
    # Way faster solution
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        options = ['A', 'C', 'G', 'T']

        q = deque([startGene])
        visit = {startGene}
        res = 0
        while q:
            for _ in range(len(q)):
                gene = q.popleft()
                if gene == endGene:
                    return res
                for j in range(8):
                    for op in options:
                        newGene = gene[:j] + op + gene[j + 1:]
                        if newGene in bankSet and newGene not in visit:
                            visit.add(newGene)
                            q.append(newGene)
            res += 1
        return -1

    # General solution, slower
    def minMutation2(self, startGene: str, endGene: str, bank: List[str]) -> int:
        patternGenes = defaultdict(list)
        bank.append(startGene)

        for gene in bank:
            for i in range(len(gene)):
                pattern = gene[:i] + '*' + gene[i + 1:]
                patternGenes[pattern].append(gene)

        visit = {startGene}
        q = deque([startGene])
        res = 0
        while q:
            for _ in range(len(q)):
                gene = q.popleft()
                if gene == endGene:
                    return res
                for j in range(len(gene)):
                    pattern = gene[:j] + '*' + gene[j + 1:]
                    for neiGene in patternGenes[pattern]:
                        if neiGene not in visit:
                            visit.add(neiGene)
                            q.append(neiGene)
            res += 1
        return -1


obj = Solution()
startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
print(obj.minMutation(startGene, endGene, bank))
