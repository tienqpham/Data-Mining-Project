from utilities import *
import numpy as np
import time
import random
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

pos_list = (
    file_to_coordinates("CWDData2015.txt")
    + file_to_coordinates("CWDData2016.txt")
    + file_to_coordinates("CWDData2017.txt")
    + file_to_coordinates("CWDData2018.txt")
    )
npdata = np.asarray(pos_list)

linked = linkage(npdata, 'single')
plt.figure()
dendrogram(linked, orientation='top', distance_sort='descending')
plt.show()

cluster = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
cluster.fit_predict(npdata)

plt.scatter(npdata[:,0], npdata[:,1], c=cluster.labels_, cmap='rainbow')
plt.show()
