class Solution:
    def gethours(self,piles,mid):
        ans = 0
        for pile in piles:
            ans += (pile+mid-1)//mid #for example:-1.4 = 2
        return ans

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while l<=r:
            mid = (l+r)//2
            if self.gethours(piles,mid) > h:
                l = mid +1
            else:
                ans = mid
                r = mid -1
        return ans
        