class Solution:
    def largestGoodInteger(self, num: str) -> str:

        res = ""
        counter = 1
        curr = num[0]
        temp = num[0]

        for i in range(1, len(num)):
            if curr == num[i]:
                counter += 1
                temp += curr
            else:
                temp = num[i]
                counter = 1

            if counter == 3:
                if res != "" and int(temp) > int(res):
                    res = temp
                elif res == "":
                    res = temp

            curr = num[i]

        return res
