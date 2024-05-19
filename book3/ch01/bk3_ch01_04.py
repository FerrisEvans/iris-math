import numpy as np

# row vector transposed to a column vector
a_row = np.array([[1, 2, 3]])

b = a_row.T

b_col = np.array([[1], [2], [3]])

a = b_col.T

A = np.array([[1, 2, 3],
              [4, 5, 6]])

A_first_col = A[:, 0]  # saved as one dimension row

A_first_col_V2 = A[:, [0]]  # saved as a column

A_first_second_col_V2 = A[:, [0, 1]]  # extract first and second columns

A_first_third_col_V2 = A[:, [0, 2]]  # extract first and third columns

A_first_row = A[[0], :]  # extract first row

A_second_row = A[[1], :]  # extract second row

A_second_row_first_col = A[[1], [0]]  # i = 2, j = 1
