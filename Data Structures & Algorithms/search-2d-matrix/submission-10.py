class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        n=len(matrix[0])-1

        for char in matrix:
            if char[0]>target:
                return False
            if char[n]< target:
                continue
            elif char[n]==target:
                return True
            elif char[n]>target:
                l=0
                r=n
                while l<=r:
                    mid=(l+r)//2
                    if char[mid]<target:
                        l=mid+1
                    elif char[mid]>target:
                        r=mid-1
                    elif char[mid]==target:
                        return True
        return False






