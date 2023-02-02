class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        result = ""
        sort_key = sorted(list(table.keys()), reverse=True)
        for val in sort_key:
            while val <= num:
                result += table[val]
                num -= val

        return result
