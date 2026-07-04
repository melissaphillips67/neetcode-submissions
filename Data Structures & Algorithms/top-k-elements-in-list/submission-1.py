class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in freqMap.items():
            buckets[freq].append(num)
        output = []
        for i in range (len(buckets)-1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if (len(output) == k):
                    return output
                

        
        
        