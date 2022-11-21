import numpy as np

a = np.arange(6)
b = a.reshape(2,3)
c = np.reshape(a, (2,3))

d = np.arange(24).reshape(2,3,4)

e = np.arange(100).reshape(2, -1)
f = np.arange(100).reshape(-1, 5)


g = np.ravel(c)

h = np.arange(10).reshape(2,-1)

print(a, a.shape)
print(b, b.shape)
print(c, c.shape)
print(d, d.shape)
print(e, e.shape)
print(f, f.shape)
print(g, g.shape)
print(h.T)