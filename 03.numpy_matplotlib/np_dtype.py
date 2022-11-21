import numpy as np

a = np.arange(5)
print(a, a.dtype)

b = a.astype('float32')
print(b, b.dtype)

c = a.astype(np.float64)
print(c, c.dtype)

d = np.uint8(a)
print(d, d.dtype)