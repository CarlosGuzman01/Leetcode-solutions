class Solution:
    def longestPalindrome(self, s: str) -> int:

        map1 = Counter(s)
        largestOdd = 'A'
        b = False

        for c in s:
            if map1[c] % 2 != 0:
                largestOdd = c
                b = True

            if b and map1[c] % 2 != 0 and map1[c] > map1[largestOdd]:
                largestOdd = c

        count = 0

        for n in map1:
            if map1[n] % 2 == 0:
                count += map1[n]
            else:
                if n == largestOdd:
                    continue
                count += (map1[n] - 1)

        if largestOdd == 'A':
            return count

        return count + map1[largestOdd]
        