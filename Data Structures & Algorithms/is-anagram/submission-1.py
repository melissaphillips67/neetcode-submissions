class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        for letter in s:
            if letter not in sMap:
                sMap[letter] = 0
            sMap[letter] += 1
        for letter in t:
            if letter in sMap:
                sMap[letter] -= 1
            else:
                return False
                
        for count in sMap.values():
            if count != 0:
                return False
        return True 

        
        