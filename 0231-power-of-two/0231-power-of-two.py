class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
        # while n % 2 == 0:
        #     n//=2

        # return n==1

    def isPowerOfTwo(self, n: int) -> bool:

        # base case 

        if n <= 0:
            return False
        if n == 1:
            return True
        if n%2 != 0:
            return False

        #Recursive case 

        return self.isPowerOfTwo(n//2)
