import math
from mpmath import mp

# Print the value of pi
print('pi = ', math.pi)

# Print the value of e
print('e = ', math.e)

# Print the value of square root of 2
print('sqrt(2) = ', math.sqrt(2))

mp.dps = 1000 + 1

print('print 1000 digits of pi behind decimal point')
print(mp.pi)

print('print 1000 digits of e behind decimal point')
print(mp.e)

print('print 1000 digits of sqrt(2) behind decimal point')
print(mp.sqrt(2))
