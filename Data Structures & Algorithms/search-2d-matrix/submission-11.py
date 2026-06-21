class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows=len(matrix)
        col=len(matrix[0])

        top=0
        bot=rows-1
        case=False

        while top<=bot:
            mid_row=(top+bot)//2
            if target>matrix[mid_row][col-1]:
                top = mid_row+1
            elif target<matrix[mid_row][0]:
                bot=mid_row-1
            else:
                case=True
                break
        
        if case:
            l=0
            r=col-1
            while l<=r:
                m=(l+r)//2

                if matrix[mid_row][m]<target:
                    l=m+1
                elif matrix[mid_row][m]>target:
                    r=m-1
                elif matrix[mid_row][m]==target:
                    return True
        return False


            





