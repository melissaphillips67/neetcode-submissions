class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol = []
        start = 0
        end = len(numbers) - 1
        while start < end:
            if (numbers[start] + numbers[end]) > target:
                end -= 1
            elif (numbers[start] + numbers[end]) < target:
                start += 1
            else:
                sol.append(start +1)
                sol.append(end +1 )
                return sol


        




        