class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for _ in range(rowIndex):
            result = [i+j for i, j in zip([0]+result, result+[0])]
        return result
