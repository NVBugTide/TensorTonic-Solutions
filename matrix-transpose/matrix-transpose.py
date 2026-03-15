import numpy as np

def matrix_transpose(A):
  A = np.asarray(A)
  transposed = A[:, :, np.newaxis] # 3D array (M, N, 1)
  transposed = transposed.swapaxes(0, 1) # (N, M, 1) - only works with 3D array
  transposed = transposed[:, :, 0]
  return transposed