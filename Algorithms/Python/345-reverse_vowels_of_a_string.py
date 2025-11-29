class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        arr = list(s)
        low = 0
        high = len(arr) - 1
        while low < high:
            while low < high and arr[low].lower() not in vowels:
                low += 1
            while low < high and arr[high].lower() not in vowels:
                high -= 1
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
            low += 1
            high -= 1

        return "".join(arr)

        