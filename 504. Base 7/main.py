class Solution:
    def convertToBase7(self, num: int) -> str:
        is_negative = num < 0
        num = divmod(abs(num), 7)
        result = str(num[1])
        while num[0]:
            num = divmod(num[0], 7)
            result = str(num[1]) + result
        return "-" * is_negative + result 
