class Solution:
    def romanToInt(self, s: str) -> int:
        roman = "IVXLCDM"
        value = [1, 5, 10, 50, 100, 500, 1000]
        table = dict(zip(roman, value))
        result = 0
        for index in range(len(s) - 1):
            if table[s[index]] < table[s[index+1]]:
                result -= table[s[index]]
            else:
                result += table[s[index]]
        return result + table[s[-1]]
