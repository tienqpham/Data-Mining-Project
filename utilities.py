import numpy
import random
import time
import math
from matplotlib import pyplot


def split_dataset(dataset, attribute):
    attributes = ["ID", "date", "county", "section", "sex", "age", "collection"]
    index = attributes.index(attribute)
    possible_values = []
    for row in dataset:
        if not row[index] in possible_values:
            possible_values.append(row[index])

    data_subsets = [None] * len(possible_values)

    for i in range(0, len(possible_values)):
        data_subsets[i] = []
        for row in dataset:
            if row[index] == possible_values[i]:
                data_subsets[i].append(row)

    return data_subsets

def plot_all_subsets(dataset):
    
    ''''''
    attributes = ["ID", "date", "county", "section", "sex", "age", "collection"]
    for attribute in attributes:
        subsets = split_dataset(dataset, attribute)
        index = attributes.index(attribute)
        for subset in subsets:
            plottable_set = list_to_coordinates(subset)
            for row, plottable_row in zip(subset, plottable_set):
                print(row)
                print(plottable_row)
            pyplot.scatter(*zip(*plottable_set))
            print(" ")
        pyplot.grid()
        pyplot.show()

    '''
    subsets_by_sex = split_dataset(dataset, "date")
    for subset in subsets_by_sex:
        pyplot.scatter(*zip(*list_to_coordinates(subset)))
    pyplot.grid()
    pyplot.show()
    ''''''
    subsets_by_age = split_dataset(dataset, "age")
    for subset in subsets_by_age:
        pyplot.scatter(*zip(*list_to_coordinates(subset)))
    pyplot.grid()
    pyplot.show()

    subsets_by_county = split_dataset(dataset, "county")
    for subset in subsets_by_county:
        pyplot.scatter(*zip(*list_to_coordinates(subset)))
    pyplot.grid()
    pyplot.show()

    subsets_by_collection = split_dataset(dataset, "collection")
    for subset in subsets_by_collection:
        pyplot.scatter(*zip(*list_to_coordinates(subset)))
    pyplot.grid()
    pyplot.show()
'''


# returns a list of values that occur for the given attribute and the number of occurences of each value
# attribute = "county" || "sex" || "age" || "collection"
def get_counts(filename, attribute):
    attributes = ["ID", "date", "county", "section", "sex", "age", "collection"]
    index = attributes.index(attribute)
    data = file_to_list(filename)
    del data[0]
    values = []
    for row in data:
        if not row[index] in values:
            values.append(row[index])

    occurrences = []

    for value in values:
        n = 0
        for row in data:
            if row[index] == value:
                n+=1
        occurrences.append([value, n])

    return occurrences

def print_counts(filename, attribute):
    data = get_counts(filename, attribute)
    for row in data:
        print(row)

def print_all_counts(filename):
    attributes = ["county", "sex", "age", "collection"]
    for attribute in attributes:
        print(attribute + ": ")
        print_counts(filename, attribute)

# converts data from file to a list of coordinates
# coordinates represent the location of any given animal

# filename = string format; name of standardized data file
# print_counts = boolean; whether or not to print counts of known and unknown location
def file_to_coordinates(filename, print_counts=False):
    height = 62
    width = 35

    instance_locations = []

    no_location = 0

    data = file_to_list(filename)
    del data[0]
    for row in data:
        if row[3] != "NoLocation":
            instance_locations.append(plss_to_indices(row[3], True))
        else:
            no_location +=1

    if print_counts:
        print("Total instances: " + str(len(data)))
        print("Instances with known location: " + str(len(instance_locations)))
        print("Instances with no known location: " + str(no_location))

    return instance_locations

def list_to_coordinates(data, print_counts=False):
    instance_locations = []

    no_location = 0
    
    for row in data:
        if row[3] != "NoLocation":
            instance_locations.append(plss_to_indices(row[3], True))
        else:
            no_location +=1

    if print_counts:
        print("Total instances: " + str(len(data)))
        print("Instances with known location: " + str(len(instance_locations)))
        print("Instances with no known location: " + str(no_location))

    return instance_locations

# returns 2D list of lists (i.e. a table) of strings
# table is constructed from tab-separated data in file
def file_to_list(filename):
    file = open(filename, 'r')
    x = file.readlines()
    file.close()

    for i in range(0, len(x)):
        x[i] = x[i].split('\t')
        deletions = 0
        j = 0
        length = len(x[i])
        while j < length:
            #print(j)
            if x[i][j] == '':
                #print(j)
                del x[i][j]
                length-=1
            j+=1

    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            for k in range(0, len(x[i][j])):
                if x[i][j][k] == '\n':
                    x[i][j] = x[i][j][0:k]

    del x[0]

    return x

# returns tuple containing the indices of a two-dimensional array
# corresponding to the coordinate position of a township on a grid

# plss_code = standardized PLSS information
# plss_code must be in the following format:
# MyyYxxXss
# M = number of meridian used for reference ( 3 || 4 )
# yy = township number
# Y = north/south cardinal reference direction from baseline ( N || S )
# xx = range number
# X = east/west cardinal reference direction from meridian ( E || W )
# ss = section number

# use_sections = whether or not to include decimal sub-coordinates

def plss_to_indices(plss_code, use_sections=False):
    # y0 = [][0] = Centralia/3rdMeridian Township 17 South
    # x0 = [0] = Beardstown/4thMeridian Range 10
    
    # Centralia Baseline/3rd Meridian, 1st Township N, 1st E, S1 = 301N01E01
    # 301N01E01 = [21][17]
    # 401N01E01 = 318N11W01
    
    # 4____xW__ : x1 = 9 - x
    # 4____xE__ : x1 = x + 9
    # 3____xW__ : x1 = 9 + ( 12 - x )
    # 3____xE__ : x1 = x + 9 + 11
    
    # 3_yS_____ : y1 = 17 - y
    # 3_yN_____ : y1 = y + 17 - 1
    # 4_yS_____ : y1 = 17 + ( 18 - y ) - 1
    # 4_yN_____ : y1 = y + 17 + 18 - 1
    reference = int(plss_code[0])
    township = int(plss_code[1:3])
    cardinal_y = plss_code[3]
    t_range = int(plss_code[4:6])
    cardinal_x = plss_code[6]
    section = int(plss_code[7:9])

    y = township
    x = t_range

    if reference == 3:
        if cardinal_y == "N":
            y = y + 17 - 1
        elif cardinal_y == "S":
            y = 18 - y - 1
            
        if cardinal_x == "E":
            x = x + 10 + 11 - 1
        elif cardinal_x == "W":
            x = 10 + (12 - x) - 1
        
    elif reference == 4:
        if cardinal_y == "N":
            y = y + 17 + 17 - 1
        elif cardinal_y == "S":
            y = 17 + ( 18 - y )
            
        if cardinal_x == "E":
            x = x + 10 - 1
        elif cardinal_x == "W":
            x = 10 - x - 1

    if use_sections:
        sub = section_to_subcoordinates(section)
        x = x + sub[0]
        y = y + sub[1]

    return [x,y]

def section_to_subcoordinates(section):
    x = 1.0
    y = 1.0
    if section%6 == 0:
        y = (6 - (section/6))/6
        x = 0
    else:
        n = math.floor(section/6)
        y = (5 - n)/6
        x = n/6

    x = round(x, ndigits=2)
    y = round(y, ndigits=2)

    return [x,y]

# converts x,y coordinates to standardized PLSS code
def indices_to_plss(location):
    pass

# converts data from file to a grid showing occurrences per township
def file_to_grid(filename):
    height = 62
    width = 35
    grid = []
    for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append(0)
        grid.append(row)

    data = file_to_list(filename)
    del data[0]
    for row in data:
        if row[3] != "NoLocation":
            pos = plss_to_indices(row[3])
            #print(pos)
            grid[ pos[1] ][ pos[0] ] +=1
            
    return grid

# converts data from file to a list of sublists
# first two elements of sublist represent coordinates where animals were found
# third element of sublist is the number of occurrences of an animal at those coordinates
# third element is always >0

# more data will be added to the return value
def file_to_density(filename):
    grid = file_to_grid(filename)
    data = []
    height = len(grid)
    width = len(grid[0])
    for i in range(0, height):
        for j in range(0, width):
            if grid[i][j] > 0:
                row = [i, j, grid[i][j]]
                data.append(row)
                
    return data

