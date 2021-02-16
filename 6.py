
#%matplotlib inline
#%%
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, solve
import math
import itertools
import random
# %%順列を求めるプログラム
num = {1, 2, 3, 4, 5} #データを定義
A = set(itertools.permutations(num, 3))
print(len(A))
for a in A:
    print(a)
# %%階乗の計算
num = {1, 2, 3, 4, 5} #データを定義
A = set(itertools.permutations(num, 5)) #numの中から5個を選ぶ順列
print(len(A))
factorial = math.factorial(5) #5の階乗を求める
print(factorial)
# %%重複順列を求める
num = {1, 2, 3, 4, 5}
A = set(itertools.product(num, num, num)) #numの中から３個を選ぶ順列
print(len(A))
for a in A:
    print(a)

# %%組み合わせを求める
num = {1, 2, 3, 4, 5}
A = set(itertools.combinations(num, 3))#numの中から３個を選ぶ組み合わせ
print(len(A)) #組み合わせが何通りあるかを確認
for a in A:
    print(a)

# %%サイコロで１の目が出る確率を求める
#サイコロをふる
cnt = 0 #1がでた数
try_cnt = 100000;
for i in range(try_cnt):
    dice = random.randint(1, 6)
    if dice == 1:
        cnt += 1
#確率を求める
p = cnt / try_cnt
print(p)

# %%全ての事象が起こる確率
#サイコロをふる
hist = [0] * 7
try_cnt = 100000;
for i in range(try_cnt):
    dice = random.randint(1, 6)
    hist[dice] += 1
#確率を求める
p = [0] * 7
for i in range(1, 7):
    p[i] = hist[i] / try_cnt
    print(i, p[i])
#確率を合計
print(sum(p))
# %%モンテカルロ法で円周率を求める
#点を描画
cnt = 0
challenge = 50000
for i in range(challenge):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    d = math.sqrt((x - 50)**2 + (y-50)**2) #中心と点の距離
    if(d <= 50):
        cnt += 1 #円の内部にある点を数える
        plt.scatter(x, y, marker='.', c='r') #赤色の点を描画
    else:
        plt.scatter(x, y, marker='.', c='g') #緑色の点を描画
plt.axis('equal')
plt.show()

#円周率を求める
p = cnt / challenge #点が円の内部にある確率
pi = p * 4 #円周率
print(pi)
# %%
