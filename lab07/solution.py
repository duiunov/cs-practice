import numpy as np


def reshape_rows(values, width):
    arr = np.asarray(values, dtype=float)

    return arr.reshape(-1, width).tolist()




























