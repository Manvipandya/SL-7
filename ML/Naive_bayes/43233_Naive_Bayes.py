import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import norm
import numpy as np


iris = sns.load_dataset("iris")
iris = iris.rename(index = str, columns = {'sepal_length':'1_sepal_length','sepal_width':'2_sepal_width', 'petal_length':'3_petal_length', 'petal_width':'4_petal_width'})

df = iris[["1_sepal_length", "2_sepal_width",'species']]
for i in range(150):
    if df.iloc[i, 2] == 'setosa':
        df.iloc[i,2] = 0
    elif df.iloc[i,2] == 'versicolor':
        df.iloc[i,2] = 1
    else:
        df.iloc[i,2] = 2


plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c = df.iloc[:, 2])
plt.xlabel('Sepa1 Length')
plt.ylabel('Sepal Width')



def predict_NB_gaussian_class(X,mu_list,std_list,pi_list): 

    scores_list = []
    classes = len(mu_list)
    
    for p in range(classes):
        score = (norm.pdf(x = X[0], loc = mu_list[p][0][0], scale = std_list[p][0][0] )  
                * norm.pdf(x = X[1], loc = mu_list[p][0][1], scale = std_list[p][0][1] ) 
                * pi_list[p])
        scores_list.append(score)
             
    return np.argmax(scores_list)


mu_list = np.split(df.groupby('species').mean().values,[1,2])
std_list = np.split(df.groupby('species').std().values,[1,2], axis = 0)
pi_list = df.iloc[:,2].value_counts().values / len(df)

prediction = np.array(  [predict_NB_gaussian_class( np.array([5,3.4]), mu_list, std_list, pi_list)] )
