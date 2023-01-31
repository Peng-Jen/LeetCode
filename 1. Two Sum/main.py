class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        buffer = {}
        for index in range(len(nums)):
            if nums[index] in buffer:
                return [buffer[nums[index]], index]
            buffer[target - nums[index]] = index
        return None
