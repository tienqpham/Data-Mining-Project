from utilities import *
import numpy as np
import time
import random
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

raw_dataset = (
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

while(True):
    #plot_kmeans(raw_dataset, 3)
    #plot_kmeans(raw_dataset, 8, True)
