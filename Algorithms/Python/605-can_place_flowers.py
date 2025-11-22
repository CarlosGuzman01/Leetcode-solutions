

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i == 0:
                if i + 1 < len(flowerbed) and flowerbed[i + 1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            else:
                if i + 1 < len(flowerbed) and flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            if n <= 0:
                return True
        return n <= 0