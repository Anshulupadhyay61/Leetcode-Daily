class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        reverse = {}

        for i in range(len(pattern)):

            if pattern[i] in mapping:
                if mapping[pattern[i]] != words[i]:
                    return False
            else:
                mapping[pattern[i]] = words[i]

            if words[i] in reverse:
                if reverse[words[i]] != pattern[i]:
                    return False
            else:
                reverse[words[i]] = pattern[i]

        return True