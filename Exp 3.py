# Define a 3x3 matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Calculate rows and columns
rows = len(matrix)
cols = len(matrix[0])

# Initialize transposed matrix
transpose_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

# Transpose the matrix
for i in range(rows):
    for j in range(cols):
        transpose_matrix[j][i] = matrix[i][j]

# Print original and transposed matrices
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transpose_matrix:
    print(row)
