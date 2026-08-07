class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightSum = []
        leftSum = []
        i = 0
        j = i +1 
        Difference = []
        
        for i in range (len(nums)):
            rightSum.append(sum(nums[i+1:]))
        for j in range (len(nums)):
                leftSum.append(sum(nums[:j]))
        for k in range (len(nums)):
            Difference.append(abs(leftSum[k] - rightSum[k]))
        return Difference

        
