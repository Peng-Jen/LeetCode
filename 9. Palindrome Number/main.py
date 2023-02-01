class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        for index in range(len(str_x) // 2):
            if str_x[index] != str_x[~index]:
                return False
        return True
