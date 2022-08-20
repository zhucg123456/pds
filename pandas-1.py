#%%
from random import random
import numpy as np
import pandas as pd
#%%
A = np.arange(6).reshape(2,-1)
B = np.arange(6).reshape(3,-1)

res = [ [sum(A[i][k] * B[k][j] 
                for k in range(A.shape[1])
            )for j in range(B.shape[1]) 
        ]for i in range(A.shape[0])
    ]
print(res)
#%%
A = np.arange(1,10).reshape(3,3)
A1 = A*A 
A2 = A@A
A3 = A.dot(A)
print(A1,A2,A3) #A2=A3矩阵乘法
#%%
B = [[A[i][j] * sum(A[i][k] for k in range(A.shape[1])
        )for j in range(A.shape[1])
    ]for i in range(A.shape[0])
]
print(B)

#%%
np.random.seed(0)
#To get a spectific stable random number(or numbers) with a given seed
A = np.random.randint(10,20,(8,5))
#print(A)
# here we cannot use A.sum(1).T 
# because a is (8,) with one dimension 
B = A.sum(0) * (A.sum(1)[:,None]) / A.sum() 
#B.shape is (A.shape[0],A.shape[1])
res = ((B-A) **2 / A) .sum()
print(res)

# %%
np.random.seed(0)
m, n, p = 100, 80, 50
B = np.random.randint(0, 2, (m, p))
U = np.random.randint(0, 2, (p, n))
Z = np.random.randint(0, 2, (m, n))

#print(B.sum()) #2544
#print(B.sum) # 缺括号，表示方法没有调用self，调用失败，返回函数方法及地址
#print(sum(B)) # B.sum(0)

# 这里的reshape和上面的[:,None]是一个意思，都是广播，为了将一维向量扩充成一维矩阵
res = (((B**2).sum(1).reshape(-1,1) + (U**2).sum(0) -2*B@U) * Z).sum()
print(res)

#%%
# 5 解答
A = np.array([1,2,5,6,7])
np.diff( np.nonzero( np.r_[1,np.diff(A)!=1,1])).max()
#%% 先diff后补全
print(np.diff(A)!=1)
print(np.r_[1,np.diff(A)!=1,1])
print(np.nonzero( np.r_[1,np.diff(A)!=1,1] ))
print(np.diff( np.nonzero( np.r_[1,np.diff(A)!=1,1] )))

#%%
#先补全后diff
B = np.array([1,2,5,5,6,7])
print(np.r_[1,B,1])
print(np.diff(np.r_[1,B,1])!=1)
print(np.nonzero(np.diff(np.r_[1,B,1])!=1))
print(np.diff(np.nonzero(np.diff(np.r_[1,B,1])!=1)))
# %%
a = np.array([0,2,5])
np.diff(a) # 返回一维数组 array([2,3])
np.nonzero(a) # 返回tuple,第一个元素是数组
np.diff(np.nonzero(a)) # 对第一个元素即数组取diff，再返回其一维数组
np.diff(np.nonzero(a)).shape # 返回二维数组,shape(1,1)