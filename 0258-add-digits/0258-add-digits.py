class Solution:
    def addDigits(self, num: int) -> int:
        # n = len(num)
        ans = 0
        
        while num >= 10:
            ans = 0

            while num > 0:
                digit = num%10
                ans += digit
                num = num//10
            num = ans
            
        return num