class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        result, p = 0, abs(x)
        while p:
            result = 10 * result + p % 10
            p //= 10
        if result >= 2 ** 31 + is_negative:
            return 0
        return result * (1-2 * is_negative)
