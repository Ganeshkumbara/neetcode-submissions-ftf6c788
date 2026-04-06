class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if not strs:
        #     return ""

        # for i in range(len(strs[0])):
        #     char = strs[0][i]
        #     for s in strs:
        #         if i == len(s) or s[i] != char:
        #             return strs[0][:i]

        # return strs[0] 

        smallestword = strs[0]

        for word in strs:
            if len(word) < len(smallestword):
                smallestword = word
        

        for word in strs:
            while not word.startswith(smallestword):
                smallestword = smallestword[:-1]
        
        return smallestword
