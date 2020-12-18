from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

iris = datasets.load_iris()

x = iris.data[:, :2]
y = iris.target

plt.scatter(x[:,0], x[:,1], c = y)
plt.xlabel('Sepa1 Length')
plt.ylabel('Sepal Width')



kmeans = KMeans(n_clusters = 3, init = 'k-means++')
kmeans.fit(x)

kcenters = kmeans.cluster_centers_
print(kcenters)


plt.scatter(kcenters[:, 0], kcenters[:, 1], c = '#ff7f0e')

            
no_clusters = 3
            
def distance(a, b):
    return (sum((a - b)**2))**0.5

def allocate_cluster(centroids, X):
    a_clusters = []
    for i in range(X.shape[0]):
        distances = []
        for c in centroids:
            distances.append(distance(c, X[i]))
        a_clusters.append(distances.index(min(distances)))
        
    return a_clusters

def calc_centroids(a_clusters, X):
    latest_centroids = []
    mean_array = {}
    for i in range(no_clusters):
        mean_array[i] = []
        
    for i in range(X.shape[0]):
        for j in range(0, no_clusters):
            if a_clusters[i] == j:
                mean_array[j].append(X[i])
                
    for i in mean_array:
        latest_centroids.append(sum(mean_array[i])/len(mean_array[i]))
                
    return latest_centroids

                
num_iters = 10
for i in range(num_iters):
    if i == 0:
        a = allocate_cluster([[6,   3.428     ], [4.81276596, 3.07446809], [3.77358491, 2.69245283]], x)
    else:
        a = allocate_cluster(w, x)
    print(a)
    w = np.array(calc_centroids(a, x))
        
        

a = allocate_cluster([[5.006,   3.428     ], [6.81276596, 3.07446809], [5.77358491, 2.69245283]], x)
        
w = calc_centroids(a, x)
