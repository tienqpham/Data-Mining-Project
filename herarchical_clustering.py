from utilities import *
import numpy as np
import time
import random
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

data = file_to_list("CWDData2017.txt")
pos_list = []
for row in data[1: ]:
    if row[3] != "NoLocation":
        pos = plss_to_indices(row[3])
        pos_list.append(pos)

npdata = np.asarray(pos_list)

linked = linkage(npdata, 'single')
plt.figure()
dendrogram(linked, orientation='top', distance_sort='descending')
plt.show()

cluster = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
cluster.fit_predict(npdata)

plt.scatter(npdata[:,0], npdata[:,1], c=cluster.labels_, cmap='rainbow')
plt.show()