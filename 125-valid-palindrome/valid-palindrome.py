class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.lower().replace(" ", "").translate(str.maketrans("","",string.punctuation))
        left, right = 0, len(clean) -1
        while left < right:
            if not clean:
                return false
            elif clean[left] == clean[right]:
                left += 1 
                right -= 1
            else:
                return False
        return True