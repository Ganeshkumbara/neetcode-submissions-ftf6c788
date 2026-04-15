class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                result[stackI] = i - stackI
            stack.append((t, i))
        
        return result 


        # for i, temp in enumerate(temperatures):
        #     ith_day = 1
        #     not_found = True
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temp:
        #             result.append(ith_day)
        #             not_found = False
        #             break
        #         else:
        #             ith_day += 1
            
        #     if not_found:
        #         result.append(0)

        # return result