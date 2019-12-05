def plss_to_grid(plss_code):
    # y0 = [][0] = Centralia/3rdMeridian Township 17 South
    # x0 = [0] = Beardstown/4thMeridian Range 10
    # Centralia Baseline/3rd Meridian, 1st Township N, 1st E, S1 = 301N01E01
    # 301N01E01 = [21][17]
    # 4____xW__ : x1 = 10 - x
    # 4____xE__ : x1 = x + 9
    # 3____xW__ : x1 = 9 + ( 13 - x )
    # 3____xE__ : x1 = x + 9 + 12
    # 3_yS_____ : y1 = 17 - y
    # 3_yN_____ : y1 = y + 17
    # 4_yS_____ : 
    # 4_yN_____ : y1 = y + 17 + 17
    reference = int(plss_code[0])
    township = int(plss_code[1:3])
    cardinal_y = plss_code[3]
    t_range = int(plss_code[4:6])
    cardinal_x = plss_code[6]
    section = int(plss_code[7:9])

    x = township
    y = t_range

    if reference == 3:
        pass
    elif reference == 4:
        pass

    if cardinal_x == "E":
        pass
    elif cardinal_x == "W":
        pass

    if cardinal_y == "N":
        pass
    elif cardinal_y == "S":
        pass
