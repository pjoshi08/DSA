import collections
from typing import List, Optional

from org.example.tree.TreeNode import TreeNode


# Most Frequent Subtree Sum: https://leetcode.com/problems/most-frequent-subtree-sum/description/
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        sumFreq = collections.defaultdict(int)

        def dfs_sum(root):
            if not root: return 0

            sum = root.val + dfs_sum(root.left) + dfs_sum(root.right)
            sumFreq[sum] += 1
            return sum

        dfs_sum(root)
        maxV = max(sumFreq.values())
        return [k for k, v in sumFreq.items() if v == maxV]
