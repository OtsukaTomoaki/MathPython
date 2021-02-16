
#%matplotlib inline
#%%
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, solve
import math

# %%行列の足し算
A = np.matrix([[50, 40], [10, 10]])
B = np.matrix([[30, 100], [20, 15]])

print(A + B)

# %%行列の掛け算
A = np.matrix([[1, 3], [2, 1]])
B = np.matrix([[150, 250], [130, 230]])

print(A * B)

# %%単位行列の掛け算
A = np.matrix([[1, 3], [2, 1]])
E = np.matrix([[1, 0], [0, 1]])
print(A * E)
print(E * A)
# %%逆行列を求める
A = np.matrix([[5, 3], [2, 1]])
B = np.linalg.inv(A) #逆行列を求める
print(B)

# %%逆行列を連立方程式でとく
A = np.matrix([[5, 3], [2, 1]])#行列A（未知数の係数で作った行列）
inv_A = np.linalg.inv(A)#行列Aの逆行列
B = np.matrix([[9], [4]])#行列B（連立方程式の右辺）
print(inv_A * B)

a = 5
b = 3
c = 2
d = 1
s = 9
t = 4
k = a * d - b * c
x = ((d/k)*s) + ((-b/k)*t)
y = ((-c/k)*s) + ((a/k)*t)
print(x, y)
# %%ベクトルと行列の掛け算
p = np.matrix([[3], [3]]) #点Pの座標
A = np.matrix([[2, 0], [1, 2]]) #変換行列A
print(A * p)
# %%図形の対称移動
#三角形ABCの頂点の経路
p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1]])

#変換行列（x軸に線対称）
A = np.matrix([[1, 0], [0, -1]])

#変換
p2 = A * p
print(p2)

#描画
p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
# %%図形の相似拡大
#三角形ABCの頂点
p = np.matrix([[1, 1, 2, 1], [3, 1, 1, 3]])

#変換行列（３倍に拡大）
A = np.matrix([[3, 0], [0, 3]])

#変換
p2 = A * p
print(p2)

#描画
p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
# %%四角形の回転
#四角形ABCDの頂点
p = np.matrix([[3, 3, 5, 5, 3], [3, 1, 1, 3, 3]])

#変換行列（反時計回りに４５度回転）
th = np.radians(45) #度数法　⇨　弧度法に変換
A = np.matrix([[np.cos(th), np.sin(-th)], [np.sin(th), np.cos(th)]])

#変換
p2 = A * p
print(p2)

#描画
p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
# %%
