class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = nums1 + nums2
        final.sort()
        n = len(final)
        if n % 2 == 0:
            ans = (final[n//2] + final[n//2 - 1])/2
            return ans
        else :
            return final[n//2]
         