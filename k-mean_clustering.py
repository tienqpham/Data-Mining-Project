from utilities import *
import numpy as np
import time
import random
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

dataset = (
    file_to_list("CWDData2015.txt")
    + file_to_list("CWDData2016.txt")
    + file_to_list("CWDData2017.txt")
    + file_to_list("CWDData2018.txt")
    )
'''
pos_list = (
    file_to_coordinates("CWDData2015.txt")
    + file_to_coordinates("CWDData2016.txt")
    + file_to_coordinates("CWDData2017.txt")
    + file_to_coordinates("CWDData2018.txt")
    )
'''
pos_list = list_to_coordinates(dataset)
npdata = np.asarray(pos_list)

kmeans = KMeans(n_clusters=3, init='random', n_init=10, max_iter=200, tol=0.0001)
y_kmeans = kmeans.fit_predict(npdata)

print(kmeans.cluster_centers_)

plt.scatter(npdata[y_kmeans == 0, 0], npdata[y_kmeans == 0, 1], s=50, c='lightgreen', marker='s', edgecolor='black')
plt.scatter(npdata[y_kmeans == 1, 0], npdata[y_kmeans == 1, 1], s=50, c='orange', marker='o', edgecolor='black')
plt.scatter(npdata[y_kmeans == 2, 0], npdata[y_kmeans == 2, 1], s=50, c='lightblue', marker='v', edgecolor='black')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=250, marker='*', c='red', edgecolor='black')

plt.grid()
plt.show()

plot_all_subsets(dataset)
