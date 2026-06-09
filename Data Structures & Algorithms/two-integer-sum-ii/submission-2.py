class Solution:
    import math
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp=round((len(numbers)/2))
        for char in numbers:
            
            print(mp)
            while mp >=0 and mp <=len(numbers):
                if char + numbers[round(mp)]<target:
                    mp=mp+mp/2
                elif char + numbers[round(mp)]>target:
                    mp=mp-mp/2
                elif char + numbers[round(mp)]==target:
                    return [char,numbers[round(mp)]]
                
                

        