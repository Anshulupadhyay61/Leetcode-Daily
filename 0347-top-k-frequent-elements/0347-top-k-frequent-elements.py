class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # 1. Frequency count
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # 2. Sort numbers according to frequency
        sorted_nums = sorted(count, key=count.get, reverse=True)

        # 3. Take first k elements
        return sorted_nums[:k]