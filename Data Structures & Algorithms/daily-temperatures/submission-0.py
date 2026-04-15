class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = []

        for i, temp in enumerate(temperatures):
            ith_day = 1
            not_found = True
            for j in range(i+1, len(temperatures)):
                print(temp, temperatures[j])
                if temperatures[j] > temp:
                    result.append(ith_day)
                    not_found = False
                    break
                else:
                    ith_day += 1
            
            if not_found:
                result.append(0)

        return result