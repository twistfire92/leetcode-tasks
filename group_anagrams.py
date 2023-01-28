# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def sorted_string(x):
            return ''.join(sorted(x))
        d = {}
        for s in strs:
            key = sorted_string(s)
            value = d.setdefault(key, [])
            value.append(s)
            d[key] = value

        return list(d.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
