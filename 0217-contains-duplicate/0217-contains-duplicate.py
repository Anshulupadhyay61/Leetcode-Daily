class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range (len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         return True    
        # return False 

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
