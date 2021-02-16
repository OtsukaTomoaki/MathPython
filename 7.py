#%matplotlib inline
#%%
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, solve
import math
import itertools
import random
import pandas as pd

# %%CSVファイルの読み込み
#score.csvの読み込み
dat = pd.read_csv('score.csv', encoding='utf-8')
print(dat.head())

# %%平均値、中央値、最頻値を求める
#score.csvの読み込み
dat = pd.read_csv('score.csv', encoding='utf-8')

#平均値、中央値
print('平均値', np.mean(dat['数学']))
print('中央値', np.median(dat['数学']))

#最頻値
bincnt = np.bincount(dat['数学']) #同じ値の個数を揃える
mode = np.argmax(bincnt) #bincntのなかで最も大きな値を取得
print('最頻値', mode)

# %%度数分布図を描画する
#score.csvの読み込み
dat = pd.read_csv('score.csv', encoding='utf-8')

#各階級に含まれる度数を数える
hist = [0]*10 #度数　（要素数10, 0で初期化）
for dat in dat['数学']:
    if dat < 10: hist[0] += 1
    elif dat < 20: hist[1] += 1
    elif dat < 30: hist[2] += 1
    elif dat < 40: hist[3] += 1
    elif dat < 50: hist[4] += 1
    elif dat < 60: hist[5] += 1
    elif dat < 70: hist[6] += 1
    elif dat < 80: hist[7] += 1
    elif dat < 90: hist[8] += 1
    elif dat <= 100: hist[9] += 1
print('度数：', hist)

#度数分布図
x = list(range(1, 11)) #x軸の値
labels = ['0~', '10~', '20~', '30~', '40~', '50~', '60~', '70~', '80~', '90~']
#x軸の目盛りラベル
plt.bar(x, hist, tick_label=labels, width=1)#棒グラフを描画
plt.show()
# %%分散と標準偏差
owner = [94, 105, 107, 106, 88] #店長の平均データ
mean = np.mean(owner) #平均
print(mean)
sum = 0
for d in owner:
    sum = sum + (d - mean)**2 #全てのデータについて「データー平均」の2乗合計を求める
print(sum)
variance = sum / len(owner)#分散
print('分散', variance)
stdev = math.sqrt(variance)
print('標準偏差', stdev)

# %%度数分布を描画する
dat = pd.read_csv('onigiri.csv', encoding='utf-8')
#度数分布表
plt.hist(dat['店長'], bins=range(0, 200, 10), alpha=0.5)
plt.hist(dat['太郎'], bins=range(0, 200, 10), alpha=0.5)
plt.show()

# %%偏差値をプログラムで求める
def def_value(score, mean, stdev):
    return (score - mean) / stdev * 10 + 50 #偏差値を計算
print(def_value(320, 278, 60))
print(def_value(430, 388, 60))

# %%
dat = pd.read_csv('score.csv', encoding='utf-8')

#散布図
plt.scatter(dat['数学'], dat['理科'])
plt.axis('equal')
plt.show()
# %%
#気温データの読み込み
dot = pd.read_csv('temperature.csv', encoding='utf-8')
n = len(dot) #データ数
x = range(1, n + 1) #x軸の数（１〜データ数）

#気温
y = dot['平均気温'] #y軸の値（平均気温）
plt.plot(x, y) #グラフを描画

#区間数：９の移動平均
v = np.ones(9) / 9.0
y2 = np.convolve(y, v, mode='same')
plt.plot(x[4:n-4], y2[4:n-4])
plt.show()
# %%回帰直線を求める
x = np.array([23, 24, 28, 24, 27, 21, 18, 25, 28, 20]) #気温
y = np.array([37, 22, 62, 32, 74, 16, 10, 69, 83, 7]) #ジュースの販売数

#回帰直線
a, b = np.polyfit(x, y, 1)
y2 = a * x + b
print(f'傾き：{a} 切片：{b}')

#描画
plt.scatter(x, y) #散布図
plt.plot(x, y2) #回帰直線
plt.show()
print(a * 31 + b) #回帰直線から未来の予測（xが33の場合のy）

# %%
