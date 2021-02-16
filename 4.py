
#%matplotlib inline
#%%
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, solve
import math

#%%ベクトルの方向を求める
rad = math.atan2(3, 2)
th = math.degrees(rad)
print(th)

# %%ベクトルの計算
a = np.array([2, 2])
b = np.array([2, -1])
print(a + b)
print(a - b)
print(2 * a)

# %% 2線のなす角度の計算
a = np.array([2, 7])
b = np.array([6, 1])
c = np.array([2, 3])
d = np.array([6, 5])

#ベクトルaとベクトルbの成分
va = b - a
vb = d - c

#ベクトルの大きさ
norm_a = np.linalg.norm(va)
norm_b = np.linalg.norm(vb)

#ベクトルの内積
dot_ab = np.dot(va, vb)

#角度を求める
cos_th = dot_ab / (norm_a * norm_b)
rad = math.acos(cos_th)
deg = math.degrees(rad)
print(deg)

# %%ベクトルの外積を求める
a = np.array([0, 1, 2])
b = np.array([2, 0, 0])
print(np.cross(a, b))

# %%
