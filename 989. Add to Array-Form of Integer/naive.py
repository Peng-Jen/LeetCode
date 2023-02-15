class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        power = len(num)
        result = num[-1]
        standard = 1
        for i in range(1, power):
            standard *= 10
            result += standard * num[~i]
        result += k
        return list(map(int, list(str(result))))
