class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = []
        for i in s.split():
            tmp.append(i)
        
        return len(tmp[-1])