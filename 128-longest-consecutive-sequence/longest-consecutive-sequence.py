class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        
        num_sorted = sorted(nums)
        longest_count = 1  
        current_streak = 1  
        
        for i in range(len(num_sorted) - 1):
            diff = num_sorted[i+1] - num_sorted[i]  
            
            if diff == 1:
                current_streak += 1 
                
            elif diff != 0:  
                longest_count = max(longest_count, current_streak)  
                current_streak = 1     
        
        return max(longest_count, current_streak)  