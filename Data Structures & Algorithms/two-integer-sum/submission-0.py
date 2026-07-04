class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range (len(nums)):
            a = target - nums[i]
            if a in myMap:
                return [myMap[a], i]
            myMap[nums[i]] = i
        return []
        