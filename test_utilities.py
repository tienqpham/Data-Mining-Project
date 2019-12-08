from utilities import *
import numpy
import time
import random
from matplotlib import pyplot

def test_file_to_coordinates():
    data = file_to_coordinates("CWDData2016.txt", True)
    for line in data:
        print(line)

def test_section_to_subcoordinates():
    for i in range(0, 10):
        k = random.randint(1,37)
        print("section " + str(k) + " = ")
        print(section_to_subcoordinates(k))

def test_file_to_list():
    data = file_to_list("CWDData2016.txt")
    for line in data:
        print(line)

def test_file_to_grid():
    grid = file_to_grid("CWDData2016.txt")
    i = len(grid)-1
    while i > -1:
        print(grid[i])
        i-=1
        pass

def test_file_to_density():
    data = file_to_density("CWDData2016.txt")
    
    pyplot.scatter(*zip(*data))
    pyplot.show()

test_file_to_coordinates()
#test_section_to_subcoordinates()
