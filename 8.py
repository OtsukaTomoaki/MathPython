#%matplotlib inline
#%%
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, solve
import math
import itertools
import random
import pandas as pd
from scipy import integrate
from PIL import Image

# %%差分グラフを描画する
#salary.csv読み込み
dat = pd.read_csv('salary.csv', encoding='utf-8')

#データをセット
x = dat['年齢']
y = dat['年収']

#グラフを描画
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()

#データ数
cnt = len(dat)

#差分をとる
diff_y = []
for i in range(0, cnt -1):
    diff_y.append(y[i + 1] - y[i])
#グラフを描画
plt.plot(x[1:], diff_y)
plt.grid(color='0.8')
plt.show()

# %%関数と導関数のグラフを描画する
#xの値
x = np.arange(-10, 10, 0.1)

#元の関数
y = x**3 + 3*x**2 + 3*x + 1
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()

#導関数
y2 = 3*x**2 + 6*x + 3
plt.plot(x, y2)
plt.grid(color='0.8')
plt.show()

# %%y=xとx軸とで囲まれた領域の面積を求める
def calc_area(dx):
    h = 0 #棒の高さ
    area = 0 #面積
    cnt = int(10 / dx) #棒の数
    for i in range(1, cnt + 1):
        h = i * dx #高さを求める
        s = h * dx #棒の面積を求める
        area += s #棒の面積を求める
    return area
print(calc_area(0.001))

# %%定積分を求める
def func(x): #基となる関数を定義
    return x**2 + 2*x + 5

integrate.quad(func, - 3, 3) #定積分を求める
# %%曲線の接線を描画する
#xの線
x = np.arange(-1, 1, 0.1)

#基の関数
y = 2*x*x + 3

#接線
a = 4*0.25 #導関数 f'(x)=4x（傾き）
b = 3.125 - a * 0.25 #切片b=y-ax
y2 = a*x + b #接線の式

#グラフの描画
plt.plot(x, y) #基の関数
plt.plot(x, y2) #接線
plt.grid(color='0.8')
plt.show()

# %%画像の輪郭を抽出する
#画像の読み込み
src_img = Image.open('sample.png')
plt.imshow(src_img)
plt.show()

#画像サイズ
width, height = src_img.size

#出力用
dst_img = Image.new('RGB', (width, height))

#カラーからモノクロへ
src_img = src_img.convert('L')

#輪郭抽出
for y in range(0, height - 1):
    for x in range(0, width - 1):
        #明るさの差を調べる
        diff_x = src_img.getpixel((x + 1, y)) - src_img.getpixel((x, y))
        diff_y = src_img.getpixel((x, y + 1)) - src_img.getpixel((x, y))
        diff = diff_x + diff_y

        #出力
        if diff >= 10:
            dst_img.putpixel((x, y), (255, 255, 255))
        else:
            dst_img.putpixel((x, y), (0, 0, 0))
plt.imshow(dst_img)
plt.show()

# %%
