import numpy as np

# --------------------
# ARRAY CREATION
# --------------------
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2], [3, 4]])

print("1D Array:", a)
print("\n2D Array:")
print(b)

print("\nShape:", b.shape)
print("Size:", b.size)
print("Data Type:", b.dtype)

# --------------------
# ARRAY OPERATIONS
# --------------------
x = np.array([10, 20, 30])
y = np.array([1, 2, 3])

print("\nAddition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

# --------------------
# SPECIAL ARRAYS
# --------------------
print("\nZeros Array:")
print(np.zeros((2, 3)))

print("\nOnes Array:")
print(np.ones((2, 3)))

print("\nRange Array:")
print(np.arange(1, 11))

# --------------------
# STATISTICS
# --------------------
arr = np.array([10, 20, 30, 40, 50])

print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# --------------------
# MATRIX OPERATIONS
# --------------------
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nMatrix Addition:")
print(A + B)

print("\nMatrix Multiplication:")
print(np.dot(A, B))

print("\nTranspose of A:")
print(A.T)

# --------------------
# RESHAPING
# --------------------
r = np.arange(1, 13)

print("\nOriginal Array:")
print(r)

print("\nReshaped Array (3x4):")
print(r.reshape(3, 4))

# --------------------
# INDEXING & SLICING
# --------------------
s = np.array([10, 20, 30, 40, 50])

print("\nFirst Element:", s[0])
print("Last Element:", s[-1])
print("Slice [1:4]:", s[1:4])

# --------------------
# STUDENT MARKS PROJECT
# --------------------
marks = np.array([
    [85, 90, 78],
    [88, 76, 92],
    [70, 80, 75]
])

print("\nStudent Marks:")
print(marks)

print("\nAverage Marks of Each Student:")
print(np.mean(marks, axis=1))

print("\nAverage Marks of Each Subject:")
print(np.mean(marks, axis=0))

print("\nHighest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))

# --------------------
# SEARCHING
# --------------------
nums = np.array([5, 10, 15, 20, 25])

print("\nIndex of 15:")
print(np.where(nums == 15))

# --------------------
# SORTING
# --------------------
unsorted = np.array([9, 2, 7, 1, 5])

print("\nSorted Array:")
print(np.sort(unsorted))

print("\nProgram Completed Successfully!")
