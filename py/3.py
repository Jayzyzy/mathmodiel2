# **************************************************************************** #
#                         画DAMN核密度图                                                     #
#                                                         :::      ::::::::    #
#    3.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Jayz <Jayzyzy@outlook.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/05 19:56:14 by Jayz              #+#    #+#              #
#    Updated: 2022/10/05 19:56:14 by Jayz             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from pickle import LIST
import matplotlib.pylab as plb
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
LISTA = [126, 149, 143, 141, 127, 123, 137, 132, 135, 134, 146, 142, 135, 141, 150, 137, 144, 137, 134, 139, 148, 144, 142, 137, 147, 138, 140, 132, 149, 131, 139, 142, 138, 145, 147, 137, 135, 142, 151, 146, 129, 120, 143, 145, 142, 136, 147, 128, 142, 132, 138, 139, 147, 128, 139, 146, 139, 131, 138, 149];


# my_list = [ 'Tom', 'Mark', 'Tony' ]

# plb.show()
# plb.close()

# 生成数据，以10000组均值为0，方差为1的高斯分布数据为例
# data = np.random.normal(0,1,100)
# print(data)
 
# n, bins, patches = plt.hist(LISTA)
# plt.show()

p1 = plt.hist(LISTA,10,density = True,color='#444693',alpha = 0.5)

df = pd.DataFrame(LISTA,columns = ['height'])
# df = sns.load_dataset('iris') 

print(df[0:10])
p1=sns.kdeplot(df['height'], shade=True)
plt.show()