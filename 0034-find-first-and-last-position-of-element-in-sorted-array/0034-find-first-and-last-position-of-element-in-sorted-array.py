class Solution:
    def searchRange(self, nums, target):

        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first, last]

    def findFirst(self, nums, target):

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return ans

    def findLast(self, nums, target):

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return ans