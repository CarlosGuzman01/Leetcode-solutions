class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            while dic[s[r]] > 2:
                dic[s[l]] -= 1
                l += 1
            ans = max(r - l + 1, ans)
        return ans
        