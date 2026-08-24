class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = s.replace(" ", "")
        tmp = []
        for i in new:
            if i.isalnum():
                tmp.append(i)
            else:
                continue
        
        cleaned = tmp
        tmp = tmp[::-1]
        final = "".join(tmp)
        final = final.lower()
        cleaned = "".join(cleaned)
        cleaned = cleaned.lower()

        if cleaned == final:
            return True
        else:
            return False