class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqToGroup = {}
        for s in strs:
            arr = [0]*26
            for letter in s:
                index = ord(letter) - ord("a")
                arr[index] += 1
            key = tuple(arr)
            if key in freqToGroup:
                freqToGroup[key].append(s)
            else:
                freqToGroup[key] = [s]
        answers = []
        for val in freqToGroup.values():
            answers.append(val)
        return answers

        