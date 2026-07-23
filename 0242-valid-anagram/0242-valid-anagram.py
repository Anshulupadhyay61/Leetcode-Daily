class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = sorted(s)
        second = sorted(t)
        
        if first == second:
            return True
        else:
            return False