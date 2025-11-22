class Solution:
    def countElements(self, nums: List[int]) -> int:

        smallest = 9999999999
        highest = -9999999999

        for n in nums:
            smallest = min(smallest, n)
            highest = max(highest, n)

        counter = 0
        for n in nums:
            if n == smallest or n == highest:
                continue
            counter += 1
        return counter 
