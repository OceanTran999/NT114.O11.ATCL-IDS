import sys
from random import random

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

path = './UNSW-NB15/'
path1 = './UNSW-NB15/'

files = os.listdir(path)
for file in files:
    pathf = os.path.join(path, file)
    data = pd.read_csv(pathf)  
    data = np.array(data)
    # print(data.shape)

    # data = data[:,:-1]
    few_data = data[:20, :-1]
    few_data = np.delete(few_data, 1, axis=1)
    few_data = np.delete(few_data, 1, axis=1)
    few_data = np.delete(few_data, 1, axis=1)
    # print(few_data.shape)
    # print(few_data[0,:])
    # sys.exit(0)
    # sample = few_data[17,:]
    s = 1
    patht = os.path.join(path1, file)
    if not os.path.isdir(patht):
        os.makedirs(patht)
    #
    for sample in few_data:
        # print(sample)
        n = 28
        matrix = np.zeros((n,n))
        # print(matrix)
        # matrix[0][0] = sample[0]
        i = 0
        for j in range(n*n):
            if (j+1)%20 == 18:
                # print((j+1)//n,(j+1)%n)
                p, q = (j+1)//n,(j+1)%n
                matrix[p][q] = sample[i]
                i = i+1
        # print(matrix)
        # print(i)
        # sys.exit(0)
        # plt.imshow(matrix, plt.cm.gray)   
        # plt.imshow(matrix)
        # plt.axis('off')
        # plt.xticks([])  
        # plt.yticks([])  
        # plt.savefig(patht+'/pic-'+str(s)+'.png', dpi=22.8, bbox_inches='tight') #plt.savefig('./img/pic-{}.png'.format(epoch + 1))


        matplotlib.image.imsave(patht + '/pic-' + str(s) + '.png', matrix)
        s = s+1
