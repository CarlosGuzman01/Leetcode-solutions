class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowel = {"a", "e", "i", "o", "u"}

        l = 0
        r = 0

        ans = 0
        curr = 0

        while r < len(s):
            if s[r] in vowel:
                curr += 1

            if r - l + 1 > k:
                if s[l] in vowel:
                    curr -= 1
                l += 1
            ans = max(curr, ans)
            r += 1
        return ans
