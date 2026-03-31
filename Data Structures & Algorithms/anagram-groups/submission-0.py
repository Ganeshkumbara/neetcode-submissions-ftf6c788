class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        removed = strs.copy()
        for i, value in enumerate(strs):
            print(strs)
            cmatch = []
            cva = Counter(value)
            if value not in removed: continue
            for j in range(i+1, len(strs)):
                if strs[j] not in removed : continue
                nva = Counter(strs[j])
                if cva == nva: cmatch.append(strs[j])
            cmatch.append(value)
            output.append(cmatch)
            # strs = [x for x in strs if x not in cmatch]
            for x in cmatch:
                removed.remove(x)
        return output