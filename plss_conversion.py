def plss_to_grid(plss_code):
    # y0 = [][0] = Centralia/3rdMeridian Township 17 South
    # x0 = [0] = Beardstown/4thMeridian Range 10
    # Centralia Baseline/3rd Meridian 1st Township N, 1st E, S1 = 301N1E01
    # 301N1E01 = [21][17]
    # 4___xW : no modification to x
    # 4___xE : 
    reference = int(plss_code[0])
    township = int(plss_code[1:3])
    lateral = plss_code[3]
    t_range = int(plss_code[4:6])
    meridial = plss_code[6]
    section = int(plss_code[7:9])
