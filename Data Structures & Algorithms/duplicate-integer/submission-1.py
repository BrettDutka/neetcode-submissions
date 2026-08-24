class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = []
        for i in nums:
            if i not in tmp:
                tmp.append(i)
            else:
                return True
        return False