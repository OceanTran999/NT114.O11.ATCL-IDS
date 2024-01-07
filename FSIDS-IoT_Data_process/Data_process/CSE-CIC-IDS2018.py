import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

path = './CSE-CIC-IDS2018/'
path1 = './CSE-CIC-IDS2018/'

files = os.listdir(path)
for file in files:
    pathf = os.path.join(path, file)
    data = pd.read_csv(pathf)  
    data = np.array(data)
    few_data = data[:20, 1:-1]
    few_data = np.delete(few_data, 1, axis=1)
    s = 1
    patht = os.path.join(path1, file)
    if not os.path.isdir(patht):
        os.makedirs(patht)
  
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
        # print(matrix)
        # sys.exit(0)
        # plt.imshow(matrix, plt.cm.gray)   #
        # plt.imshow(matrix)
        # plt.axis('off')
        # plt.savefig(patht+'/pic-'+str(s)+'.png', dpi=22.8, bbox_inches='tight') #plt.savefig('./img/pic-{}.png'.format(epoch + 1))

        
        matplotlib.image.imsave(patht + '/pic-' + str(s) + '.png', matrix)
        s = s+1
