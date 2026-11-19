import numpy as np


hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)


print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)

print('\n')

print(line)
print(zeros)
print(unknown_table)
print(identity)

print('\n')

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])

print('\n')

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures)
print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print('\n')
print(temperatures[1,2])
print(temperatures[0])
print('\n')
print(temperatures[:,-1])
print('\n')
print(temperatures[:2,1:])
print('\n')
print(temperatures[0:2,1:3])


matrix = np.arange(1, 26).reshape(5, 5)
print('\n')
print(matrix)

print('\n')
print(matrix[0:3])
print(matrix[0:3].shape)

print('\n')
print(matrix[:,0:2])
print(matrix[:,0:2].shape)

print('\n')
print(matrix[-2:])
print(matrix[-2:].shape)

print('\n')
print(matrix[1:4,2:5])
print(matrix[1:4,2:5].shape)

print('\n')
print(matrix[-2:,-2:])
print(matrix[-2:,-2:].shape)


vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1
print('\n')
print(hours)
print('\n')
print(changed_hours)

changed_matrix = matrix.copy()
changed_matrix[1] = 0
changed_matrix[:,-1] = -1
changed_matrix[1:4,1:4] = 100
print('\n')
print(changed_matrix)
print('\n')
print(matrix)


numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T


print('\n')
print(numbers.shape)
print(table.shape)
print(transposed.shape)