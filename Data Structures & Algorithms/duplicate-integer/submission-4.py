class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for iteam in nums:
            if iteam not in hashset:
                hashset.add(iteam)
            else:
                return True
        return False