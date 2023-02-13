class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (nums := high - low + 1) % 2 * (low % 2) + nums // 2 
