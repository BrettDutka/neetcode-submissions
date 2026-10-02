class Solution:
    def countSeniors(self, details: List[str]) -> int:
        above = 0
        for i in details:
            if int(i[11] + i[12]) > 60:
                above += 1
        
        return above

