class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1,r1 = 0,len(matrix)-1
        len_r = len(matrix[0])-1
        while l1 <= r1:
            mid1 = (l1+r1)//2
            if matrix[mid1][0] <= target and matrix[mid1][len(matrix[0])-1] >= target:
                return self.search_in_col(matrix,mid1,target)
            elif matrix[mid1][0] < target:
                l1 = mid1 +1
            else:
                r1 = mid1 -1
        return False
    

    def search_in_col(self,matrix, row, target):
        l,r = 0,len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False