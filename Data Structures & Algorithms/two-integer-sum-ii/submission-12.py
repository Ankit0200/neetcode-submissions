class Solution:
    import math
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for char in numbers:
            mp=round((len(numbers)/2))
            
            print(mp)
            while mp >=0 and mp <=len(numbers):
                print("CAME HERE")
                print(mp,"&&")
                if char + numbers[round(mp)]<target:
                    new_mp=round(mp+mp/2)
                    if new_mp==mp and mp==len(number):
                        break
                    mp=new_mp
                elif char + numbers[round(mp)]>target:
                    
                    mp=round(mp-mp/2)

                elif char + numbers[round(mp)]==target:
                    return [numbers.index(char)+1,int(mp+1)]
                
                

        