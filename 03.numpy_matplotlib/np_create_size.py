import numpy as np

a = np.empty((2,3))
b = np.empty((2,3), dtype=np.int16)
c = np.zeros((2,3))
d = np.zeros((2,3), dtype=np.int8)
e = np.ones((2,3), dtype=np.float32)
f = np.full((2,3,4), 255, dtype=np.uint8)

print(a, a.dtype, a.shape)
a.fill(255)
print(a)
print(b, b.dtype, b.shape)
print(c, c.dtype, c.shape)
print(d, d.dtype, d.shape)
print(e, e.dtype, e.shape)
print(f, f.dtype, f.shape)