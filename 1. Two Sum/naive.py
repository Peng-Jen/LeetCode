class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index in range(len(nums)-1):
            remaining = target - nums[index]
            nums[index] = None
            if remaining in nums[index + 1:]:
                return [index, nums.index(remaining)]
        return None
