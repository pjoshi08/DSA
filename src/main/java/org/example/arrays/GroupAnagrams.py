

class Solution(object):

    def groupAnagrams(self, strs):
        dict = defaultdict(list)

        for str in strs:
            count = [0] * 26  # a .... z

            for c in str:
                count[ord(c) - ord("a")] += 1
            dict[tuple(count)].append(str)

        return dict.values()


    # Time Limit Exceeded
    def groupAnagrams2(self, strs):
        if len(strs) == 1:
            return [[strs[0]]]

        dict = {strs[0]: [strs[0]]}

        for str in strs[1:]:
            added = False
            for key in dict.keys():
                if self.isAnagram(key, str):
                    dict[key].append(str)
                    added = True
                    break
            if not added:
                dict[str] = [str]
        return list(dict.values())

    def isAnagram(self, str1, str2):
        if len(str1) != len(str2): return False
        dict1 = {}
        for c in str1:
            dict1[c] = dict1.get(c, 0) + 1
        dict2 = {}
        for c in str2:
            dict2[c] = dict2.get(c, 0) + 1

        for c in str1:
            if dict1[c] != dict2.get(c, 0):
                return False
        return True


obj = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ["","b"]
print(obj.groupAnagrams(strs))
