class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix = 0
        freq = {0: 1}

        for num in nums:
            prefix += num

            required = prefix - k

            if required in freq:
                count += freq[required]

            freq[prefix] = freq.get(prefix, 0) + 1

        return count