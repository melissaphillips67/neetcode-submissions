class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myArray = []
        for i in range (len(nums)):
            if nums[i] in myArray:
                return True
            myArray.append(nums[i])
        return False
        