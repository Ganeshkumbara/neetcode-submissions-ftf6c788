class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append('counter')
        return '.'.join(strs)
    def decode(self, s: str) -> List[str]:
        res = s.split('.')[:-1]
        return res
