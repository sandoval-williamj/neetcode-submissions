class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset = set()

        for num in nums:
            if num not in myset:
                myset.add(num)
            else:
                return num