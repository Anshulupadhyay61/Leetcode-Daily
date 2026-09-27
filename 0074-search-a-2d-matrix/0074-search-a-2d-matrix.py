class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        column = len(matrix[0])

        l = 0
        r = rows*column - 1
        while l<=r:
            mid = (l+r)//2
            i = mid//column
            j = mid%column

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mid - 1 #left
            else :
                l = mid + 1 #right
        return False
