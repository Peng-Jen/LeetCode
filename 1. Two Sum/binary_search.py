class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = list(enumerate(nums))
        nums.sort(key=lambda x: x[1])
        for index in range(len(nums)-1):
            right, left = len(nums) - 1, index + 1
            if nums[index][1] + nums[right][1] < target or nums[index][1] + nums[left][1] > target:
                continue
            for boundary in [right, left]:
                if nums[index][1] + nums[boundary][1] == target:
                    return [nums[index][0], nums[boundary][0]]
            while right - left > 1:
                mid = (right + left + 1) // 2
                if nums[index][1] + nums[mid][1] > target:
                    right = mid
                elif nums[index][1] + nums[mid][1] < target:
                    left = mid
                elif nums[index][1] + nums[mid][1] == target:
                    return [nums[index][0], nums[mid][0]]
        return None
