
#%matplotlib inline
#%%
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, solve
import math

#%%

x = [1, 2, 3, 4, 5, 6, 7]
y = [64.3, 63.5, 63.6, 64.0, 63.5, 63.2, 63.1]

plt.plot(x, y)
plt.grid(color='0.8')
plt.show()

# %%
x = list(range(1, 11))
y = []
for i in range(10):
    y.append(3 * x[i] - 24)
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()
# %%

x = np.arange(-1.0, 1.01, 0.01)
y = 3 * x

plt.plot(x, y)
plt.grid(color='0.8')
plt.show()
# %%
a = Symbol('a')
b = Symbol('b')

ex1 = a + b - 1
ex2 = 5 * a + b - 3

print(solve((ex1, ex2)))

# %%
x = np.arange(-1, 6)
y = 1/2 * x + 1/2
y2 = -2 * x + 7

plt.plot(x, y)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()

# %%
#基となる線分の傾きと切片
a1 = (5-1)/(6-0)
b1 = 1
#線分の中点
cx = (0 + 6) / 2
cy = (1 + 5) / 2
#線分に直交する直線の傾き（a2 = -1/a1）
a2 = -1 / a1

#線分に直交する直線の切片（b2 = y - a2*x）
b2 = cy - a2*cx

#直線の式
x = np.arange(0, 7) #xの値
y1 = a1*x + b1 #元の直線
y2 = a2*x + b2 #垂直二等分線

#描画
plt.plot(x, y1)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()


# %% 三角関数を使って円を描画
#角度
th = np.arange(0, 360, 90)

#演習場の点Pの座標
x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

#描画
plt.plot(x, y)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()

# %%円の方程式
r = 300 #半径
x = np.arange(-r, r + 1)
y = np.sqrt(r**2 - x**2)
y1 = np.sqrt(r**2 - x**2) * -1
#描画
plt.plot(x, y)
plt.plot(x, y1)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()

# %%中心が（0, 0）以外の円を描画

#円の中心
a = 200
b = 300

#円の方程式
r = 300 #半径
x = np.arange(a-r, a+r+1) #x : (200, 300)を中心に半径300の円を描くために必要な範囲

y = np.sqrt(r**2 - (x-a)**2) + b #円の上側
y2 = -y + 2*b #円の下側

#描画
plt.plot(x, y)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()

# %%ヘロンの公式
x = [1, 3, 6] #x座標（A,B,C）
y = [5, 1, 4] #y座標（A,B,C）
a = math.sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2) #辺ABの長さ
b = math.sqrt((x[2] - x[1]) ** 2 + (y[2] - y[1]) ** 2) #辺BCの長さ
c = math.sqrt((x[2] - x[0]) ** 2 + (y[2] - y[0]) ** 2) #辺ACの長さ

s = (a + b + c) / 2
print(math.sqrt(s * (s-a) * (s-b) * (s-c))) #ヘロンの公式

# %%
