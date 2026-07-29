class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0

        for s in sentences:
            words = s.split()
            count = len(words)

            if count > maximum:
                maximum = count
        return maximum