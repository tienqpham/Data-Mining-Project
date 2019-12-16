from utilities import *
import numpy
import time
import random
from matplotlib import pyplot

DATA_2016 = "CWDData2016.txt"
DATA_2015 = "CWDData2015.txt"

def test_file_to_coordinates(test_age = False):
    data = file_to_coordinates(DATA_2015, test_age, True)
    for line in data:
        print(line)
    pyplot.scatter(*zip(*data))
    pyplot.show()

def test_section_to_subcoordinates():
    for i in range(0, 10):
        k = random.randint(1,37)
        print("section " + str(k) + " = ")
        print(section_to_subcoordinates(k))

def test_file_to_list():
    data = file_to_list(DATA_2015)
    for line in data:
        print(line)

def test_file_to_grid():
    grid = file_to_grid(DATA_2016)
    i = len(grid)-1
    while i > -1:
        print(grid[i])
        i-=1
        pass

def test_file_to_density():
    data = file_to_density(DATA_2016)
    
    pyplot.scatter(*zip(*data))
    pyplot.show()

def test_get_counts():
    data = get_counts(DATA_2016, "collection")
    for row in data:
        print(row)

def test_split_dataset():
    data = file_to_list(DATA_2016)
    subsets = split_dataset(data, "age")
    for subset in subsets:
        for row in subset:
            print(row)
        print(" ")

test_file_to_coordinates(True)
#test_section_to_subcoordinates()
#test_get_counts()
#test_file_to_list()
#print_all_counts(DATA_2016)
#test_split_dataset()
