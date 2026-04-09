
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        bracket_dict = {
            ')': '(',
            '}': '{',
            ']': '['
            }

        for char in s:

            if char in bracket_dict:
                if not stack or stack.pop() != bracket_dict[char]:
                    return False
            else:
                stack.append(char)

        return not stack
