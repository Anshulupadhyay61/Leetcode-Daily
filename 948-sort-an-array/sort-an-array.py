class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Base Case
        if len(nums) <= 1:
            return nums

        # Divide
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # Recursively sort both divided array
        left = self.sortArray(left)
        right = self.sortArray(right)

        # Merge both sorted aarays 
        return self.merge(left, right)

    def merge(self, left, right):

        result = []
        i = 0
        j = 0

        # Compare elements of both arrays
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Remaining elements of left array
        while i < len(left):
            result.append(left[i])
            i += 1

        # Remaining elements of right array
        while j < len(right):
            result.append(right[j])
            j += 1

        return result