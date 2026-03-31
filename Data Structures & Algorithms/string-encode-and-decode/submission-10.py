# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         res = []
#         if len(strs) <= 1 :
#             res.append(strs[0])
#             return res
#         else:return '.'.join(strs)
#     def decode(self, s: str) -> List[str]:
#         if len(s) <= 1 :
#             return s
#         else:return s.split('.')

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
