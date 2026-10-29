import numpy as np


def reshape_rows(values, width):
    if len(values) % width != 0:
        return []

    arr = np.asarray(values, dtype=float)
    return arr.reshape(-1, width).tolist()


def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype=float)
    return arr[np.ix_(rows, columns)].tolist()

def column_means(matrix):
    if len(matrix) == 0:
        return []

    arr = np.asarray(matrix, dtype=float)
    return np.round(np.mean(arr, axis=0), 6).tolist()


def column_range(matrix, column):
    arr = np.asarray(matrix, dtype=float)
    col_data = arr[:, column]
    return float(np.round(np.max(col_data) - np.min(col_data), 6))























