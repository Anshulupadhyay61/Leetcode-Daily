class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        maximum_no = max(nums)
        frequency = [0]*(maximum_no + 1)

        for i in nums:
            frequency[i] += 1
        index = 0
        for i in range(0,maximum_no + 1):
            while frequency[i] > 0:
                nums[index] = i
                index += 1
                frequency[i] -= 1
        
        