class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            num1 = target - num
            if num1 in nums[i + 1:]:
                j = nums.index(num1, i + 1)
                return [i, j]
