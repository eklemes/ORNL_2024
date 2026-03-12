import numpy as np
import random
import math



def rand_org(r):
    pitch=0.0074125
    max_x =math.floor((pitch-r)*10000000)
    org_x = random.randint(-max_x, max_x)/10000000
    max_y = math.floor((pitch-r)*10000000)
    org_y = random.randint(-max_y, max_y)/10000000
    max_z = math.floor((pitch-r)*10000000)
    org_z = random.randint(-max_z, max_z)/10000000
    return org_x, org_y, org_z


part_path = "/Users/eiriniklemes/Documents/ORNL/project_1/python/partial_files//"
dest_path = '/Users/eiriniklemes/Documents/ORNL/project_1/python/py_samp//'
temp_file = '/Users/eiriniklemes/Documents/ORNL/project_1/models/small_plate/sampler/base_keno_C1.5_small.inp'

for cases in range(1, 11):
    f = open(f'{part_path}sphere_loc_gens{cases}.part', "w")
    for i in range(934627):#:
       r = 0.005 
       x_org, y_org, z_org = rand_org(r)
       #print(f" ellipsoid 11 {a} {b} {c} origin x={x_org} y={y_org} z={z_org}")
       f.write(f"unit {i+201}\n   sphere 11 0.005 origin x={x_org} y={y_org} z={z_org}  media 110 1 11\n   cuboid 12 6p0.0074125   media 60 1 12 -11 \n boundary 12 \n")
    f.close()
   
    with open(f'{part_path}sphere_loc_gens{cases}.part', "r") as f:
        og_cont = f.read()
        
    with open(temp_file, "r") as temp:
        temp_keno = temp.read()
    
    new_content = temp_keno.replace("'insert", og_cont)
    more_cont = temp_keno.replace("934624i201 934626", "934626i201 934827")
    with open(f'{dest_path}keno_spheres_loc{cases}.inp', "w") as dest:
        dest.write(new_content)
        dest.write(more_cont)

