class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        for _ in range(1, numRows):
            (last := result[-1].copy()).append(0)
            last_reverse = last[::-1]
            for index in range(len(last)):
                last[index] += last_reverse[index]
            result.append(last)
        return result

