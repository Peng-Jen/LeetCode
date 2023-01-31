class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        for _ in range(1, numRows):
            result.append(
                list(map(lambda x, y: x+y, [0]+result[-1], result[-1]+[0])))
        return result
