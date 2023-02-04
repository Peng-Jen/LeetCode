class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        counter, index = 0, 0
        length = len(nums)
        while index + counter < length:
            if nums[index] == val:
                nums.pop(index)
                counter += 1
                continue
            index += 1
        return length - counter
 