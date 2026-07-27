class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s = sum(x for x in nums if x < 10)
        return s != sum(nums) - s
        #complete