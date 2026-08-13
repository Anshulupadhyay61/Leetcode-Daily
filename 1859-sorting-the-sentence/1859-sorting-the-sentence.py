class Solution:
    def sortSentence(self, s: str) -> str:
        word = s.split()
        ans = [""]*len(word)
        for i in range (len(word)):
            number = int(word[i][-1])
            ans[number - 1] = word[i][:-1]
        return " ".join(ans)
        
