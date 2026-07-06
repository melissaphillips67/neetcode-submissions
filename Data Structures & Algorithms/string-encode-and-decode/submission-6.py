class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = ""
        for s in strs:
            lengths += str(len(s)) + "#" + s
        return lengths


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])  
            strs.append(s[j+1 : j + 1 + length])
            i = j + 1 + length
            j = i 
        return strs
