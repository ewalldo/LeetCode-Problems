class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {}
        ans = 0
        start = 0
        for i,v in enumerate(s):
            if v in dicts:
                sums = dicts[v] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > ans:
                ans = num
            dicts[v] = i
        return ans
