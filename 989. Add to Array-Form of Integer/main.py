class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        return list(map(int, str(int(''.join([str(n) for n in num])) + k)))
