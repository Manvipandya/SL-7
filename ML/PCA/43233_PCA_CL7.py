


import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt


def getMNIST():
    
    data = pd.read_csv('train.csv').as_matrix().astype(np.float32)
    Xtrain = data[:35000, 1:] / 255
    Ytrain = data[:35000, 0].astype(np.int32)
    
    Xtest = data[35000:, 1:] / 255
    Ytest = data[35000:, 0].astype(np.int32)
    
    return Xtrain, Ytrain, Xtest, Ytest



    
pca = PCA()
Xtrain, Ytrain, Xtest, Ytest = getMNIST()
reduced = pca.fit_transform(Xtrain)
    
plt.scatter(reduced[:,0], reduced[:,1], s=100, c=Ytrain, alpha=0.5)
plt.show()
    
plt.plot(pca.explained_variance_ratio_)
plt.show()
    
cumulative = []
last = 0
for v in pca.explained_variance_ratio_:
    cumulative.append(last + v)
    last = cumulative[-1]

plt.plot(cumulative)
plt.show()
