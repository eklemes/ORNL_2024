import numpy as np
import random
import math

def rand_gen():
    return random.randint(10000,74123)/10000000
def dim_gen():
    vol = 5.236112004316330E-07
    a = rand_gen()
    b = rand_gen()
    c = (vol*3)/(4*math.pi *a*b)
    return a, b, c

'''
og_path = 'C:\\Users\\ek2\\OneDrive - Oak Ridge National Laboratory\\Desktop\\python\\partial_files\\'
dest_path = 'C:\\Users\\ek2\\OneDrive - Oak Ridge National Laboratory\\Desktop\\scale_models\\py_samp\\'
temp_file = 'C:\\Users\\ek2\\OneDrive - Oak Ridge National Laboratory\Desktop\\models\\base_keno_small.inp'
'''
og_path = "/Users/eiriniklemes/Documents/ORNL/project_1/python/partial_files/ellipsoids//"
dest_path = '/Users/eiriniklemes/Documents/ORNL/project_1/python/py_samp/ellipsoids//'
temp_file = '/Users/eiriniklemes/Documents/ORNL/project_1/models/small_plate/sampler/base_keno_ellipsoid.inp'

for cases in range(21, 31):
    f = open(f'{og_path}ellipsoid_size_gen{cases:03}.part', "w")  
    for i in range(934627):
        a, b, c = dim_gen()
        while c >= 0.0074125:
            a, b, c = dim_gen()
        vol_ch= (3/4) * np.pi * a * b * c
        f.write(f"unit {i+201}\n   ellipsoid 11 {a} {b} {c}   media 110 1 11\n   cuboid 12 6p0.0074125   media 60 1 12 -11 \n boundary 12 \n")
    f.close()
    
    with open(f'{og_path}ellipsoid_size_gen{cases:03}.part', "r") as f:
        og_cont = f.read()
        
    with open(temp_file, "r") as temp:
        temp_keno = temp.read()
    
    new_content = temp_keno.replace("'insert", og_cont)
    
    with open(f'{dest_path}keno_ellipsoids{cases:03}.inp', "w") as dest:
        dest.write(new_content)
f.close()
