class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            numsSet.add(num)
        longest = 0 
        for num in numsSet:
            previous = num - 1
            if previous not in numsSet:
                length = 1
                current = num
                while current + 1 in numsSet:
                    length += 1
                    current += 1
                longest = max(longest, length)
        return longest
        