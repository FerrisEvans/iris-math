import numpy as np

a_i = np.linspace(1, 10, 10)
print(a_i)

a_i_cumprod = np.cumprod(a_i)
np.set_printoptions(suppress=True)
print(a_i_cumprod)
