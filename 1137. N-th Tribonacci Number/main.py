class Solution:
    def tribonacci(self, n: int) -> int:
        prev_3 = [0, 1, 1]
        if n < 3:
            return prev_3[n]
        for _ in range(n-2):
            prev_3.append(sum(prev_3))
            prev_3.pop(0)
        return prev_3[-1]
