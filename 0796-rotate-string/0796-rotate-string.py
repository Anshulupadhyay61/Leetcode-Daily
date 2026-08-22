class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        ans = s + s
        if goal in ans:
            return True
        return False
        