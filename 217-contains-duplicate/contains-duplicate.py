from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ctr = Counter(nums)
        for num in nums:
            if ctr[num] >= 2:
                return True
        return False        
              