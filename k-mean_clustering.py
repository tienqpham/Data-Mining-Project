from utilities import *
import numpy as np
import time
import random
import sys
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

again = "y"
while(again != "n"):
    print("Clustering 2D data")
    k = input("d=2, k = ")
    type(k)
    
    if(represents_int(k)):
        k = int(k)
        plot_kmeans(raw_dataset, k)
    else:
        print("invalid k value")

    again = input("again? (y/n)")
    type(again)


again = "y"
while(again != "n"):
    print("Clustering 3D data")
    k = input("d=3, k = ")
    type(k)
    
    if(represents_int(k)):
        k = int(k)
        plot_kmeans(raw_dataset, k, True)
    else:
        print("invalid k value")

    again = input("again? (y/n)")
    type(again)

    

#plot_all_subsets(raw_dataset)
