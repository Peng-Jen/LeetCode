class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(len(a))
        result = ""
        carry = False
        for i in range(len(a)):
            bit = (temp := (int(a[~i]) + int(b[~i]) + carry)) % 2
            carry = temp // 2
            result += str(bit)
        if carry == 1:
            return (result + "1")[::-1]
        return result[::-1]
