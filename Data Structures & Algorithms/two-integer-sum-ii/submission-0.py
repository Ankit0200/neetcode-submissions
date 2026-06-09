class Solution:
    import math
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp=math.floor((len(numbers)/2))
        for char in numbers:
            
            print(mp)
            while mp >=0 and mp <=len(numbers):
                if char + numbers[mp]<target:
                    mp=int(mp+mp/2)
                elif char + numbers[mp]>target:
                    mp=int(mp-mp/2)
                elif char + numbers[mp]==target:
                    return [char,numbers[mp]]
                
                

        