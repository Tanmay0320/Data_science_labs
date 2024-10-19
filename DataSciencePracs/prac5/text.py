rows = 5
cols = 3
depth = 7

matrix = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(depth)]

def update_matrix(matrix):
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                index_sum = d + r + c
                if (index_sum % 10 == 4) or (index_sum % 10 == 6) :
                    matrix[d][r][c] = 0
                else:
                    matrix[d][r][c] = 1
    return matrix

def findit(matrix):
    largest = 0
    final = []

    # Check rows
    for d in range(depth):
        for r in range(rows):
            count = 0
            temp_list = []
            for c in range(cols):
                if matrix[d][r][c] == 1:
                    count += 1
                    temp_list.append([r, c, d])
                else:
                    if count > largest:
                        largest = count
                        final = temp_list.copy()
                    temp_list.clear()
                    count = 0
        if count > largest:
            largest = count
            final = temp_list.copy()

    # Check columns
    for d in range(depth):
        for c in range(cols):
            count = 0
            temp_list = []
            for r in range(rows):
                if matrix[d][r][c] == 1:
                    count += 1
                    temp_list.append([r, c, d])
                else:
                    if count > largest:
                        largest = count
                        final = temp_list.copy()
                    temp_list.clear()
                    count = 0
        if count > largest:
            largest = count
            final = temp_list.copy()

    # Check depths
    for r in range(rows):
        for c in range(cols):
            count = 0
            temp_list = []
            for d in range(depth):
                if matrix[d][r][c] == 1:
                    count += 1
                    temp_list.append([r, c, d])
                else:
                    if count > largest:
                        largest = count
                        final = temp_list.copy()
                    temp_list.clear()
                    count = 0
        if count > largest:
            largest = count
            final = temp_list.copy()
            
    print(f"Length of the largest contiguous subarray of 1s : {largest}")
    print("Coordinates of the largest contiguous subarray of 1s:")
    print(final)

updated_matrix = update_matrix(matrix)

for d in updated_matrix:
    for r in d:
        print(r)
    print("-----")

findit(updated_matrix)