class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0 
        right = len(s)-1
        vowel = "aeiouAEIOU"
        s = list(s)

        while left < right:
            if s[left] not in vowel:
                left += 1
            elif s[right] not in vowel:
                right -= 1
            else:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
        return "".join(s)

        