class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for word in strs:
            key = "".join(sorted(word))
            hashmap[key] = hashmap.get(key, []) + [word]


        return list(hashmap.values())