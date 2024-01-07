import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

path = './CIC-IDS2017/'
path1 = './CIC-IDS2017/'

files = os.listdir(path)
for file in files:
    pathf = os.path.join(path, file)
    data = pd.read_csv(pathf) 
    data = np.array(data)
    few_data = data[:20, 1:-1]
    # print(few_data.shape)
    # print(few_data[0, :])
    # sys.exit(0)
    # print(few_data.shape)
    # print(few_data[0,:])
    # sample = few_data[17,:]
    patht = os.path.join(path1, file)
    if not os.path.isdir(patht):
        os.makedirs(patht)
    s = 1
    for sample in few_data:
        # print(sample)
        n = 28
        matrix = np.zeros((n,n))
        # print(matrix)
        # matrix[0][0] = sample[0]
        i = 0
        for j in range(n*n-10):
            if (j+1)%10 == 6:
                # print((j+1)//n,(j+1)%n)
                p, q = (j+1)//n,(j+1)%n
                matrix[p][q] = sample[i]
                i = i+1


        matplotlib.image.imsave(patht + '/pic-' + str(s) + '.png', matrix)


        s = s+1
