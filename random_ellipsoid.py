import numpy as np
import random
import math

def rand_size():
    return random.randint(10000,74123)/10000000

def rand_org(a,b,c):
    pitch=0.0074125
    max_x =math.floor((pitch-a)*10000000)
    org_x = random.randint(-max_x, max_x)/10000000
    max_y = math.floor((pitch-b)*10000000)
    org_y = random.randint(-max_y, max_y)/10000000
    max_z = math.floor((pitch-c)*10000000)
    org_z = random.randint(-max_z, max_z)/10000000
    return org_x, org_y, org_z

def dim_gen():
    vol = 5.236112004316330E-07
    a = rand_size()
    b = rand_size()
    c = (vol*3)/(4*math.pi *a*b)
    return a, b, c

'''
og_path = 'C:\\Users\\ek2\\OneDrive - Oak Ridge National Laboratory\\Desktop\\python\\partial_files\\'
dest_path = 'C:\\Users\\ek2\\OneDrive - Oak Ridge National Laboratory\\Desktop\\scale_models\\py_samp\\'
#mp_file = 'C:\\Users\\ek2\\OneDrive - Oak Ridge National Laboratory\Desktop\\models\\base_keno_small.inp'
temp_file = 'C:\\Users\\ek2\\OneDrive - Oak Ridge National Laboratory\\Desktop\\scale_models\\base_keno_ellipsoid.inp'
'''

og_path = "/python/partial_files/ellipsoids//"
dest_path = '/python/py_samp/ellipsoids//'
temp_file = '/models/small_plate/sampler/base_keno_ellipsoid.inp'


for cases in range(51, 101):
    f = open(f'{og_path}ellipsoid_size_loc_gens{cases:03}.part', "w")
    for i in range(934627):#:
        a, b, c = dim_gen()
       #print(i)
        while c >= 0.0074125:
            a, b, c = dim_gen()
        #vol_ch= (3/4) * np.pi * a * b * c
        x_org, y_org, z_org = rand_org(a,b,c)
       #print(f" ellipsoid 11 {a} {b} {c} origin x={x_org} y={y_org} z={z_org}")
        f.write(f"unit {i+201}\n   ellipsoid 11 {a} {b} {c} origin x={x_org} y={y_org} z={z_org}  media 110 1 11\n   cuboid 12 6p0.0074125   media 60 1 12 -11 \n boundary 12 \n")
    f.close()
   
    with open(f'{og_path}ellipsoid_size_loc_gens{cases:03}.part', "r") as f:
        og_cont = f.read()
        
    with open(temp_file, "r") as temp:
        temp_keno = temp.read()
    
    new_content = temp_keno.replace("'insert", og_cont)
    
    with open(f'{dest_path}keno_ellipsoids_size_loc{cases:03}.inp', "w") as dest:
        dest.write(new_content)
        
f.close()