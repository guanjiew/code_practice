def searchMatrix(matrix, target):
    if not matrix:
        return False
    if target < matrix[0][0]:
        return False
    # find the index which target might appear in first row
    row_idx = -1
    if target <= matrix[0][-1]:
        i = 0
        j = len(matrix[0]) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if matrix[0][mid] == target:
                return True
            elif matrix[0][mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        row_idx = j
    col_id = -1
    if target <= matrix[-1][0]:
        i = 0
        j = len(matrix) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                i = mid + 1
            else:
                j = mid - 1
        col_id = j

    if col_id != -1 and row_idx != -1:
        return target == matrix[col_id][row_idx]
    else:
        # element must be last row or last column
        i = 0
        j = len(matrix) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target:
                i = mid + 1
            else:
                j = mid - 1
        i = 0
        j = len(matrix[-1]) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if matrix[-1][mid] == target:
                return True
            elif matrix[-1][mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
print(searchMatrix(matrix, target))
