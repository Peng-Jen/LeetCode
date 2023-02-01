class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        result, p = 0, x
        while p:
            result = 10 * result + p % 10
            p //= 10
        return result == x
