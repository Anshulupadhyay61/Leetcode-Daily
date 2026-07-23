class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Step 1: Roman to Integer mapping
        roman = {
            'I': 1,   # 1
            'V': 5,   # 5
            'X': 10,  # 10
            'L': 50,  # 50
            'C': 100, # 100
            'D': 500, # 500
            'M': 1000 # 1000
        }

        total = 0  # final answer

        # Step 2: Traverse the string
        for i in range(len(s)):

            # Check if next element exists AND current < next
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]   # subtract case
            else:
                total += roman[s[i]]   # normal add

        return total  # return result