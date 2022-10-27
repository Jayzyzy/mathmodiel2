# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    txttocsv.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Jayz <Jayzyzy@outlook.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/27 12:29:16 by Jayz              #+#    #+#              #
#    Updated: 2022/10/27 12:29:16 by Jayz             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ast import Try
from calendar import c
import os

FILELC = '24'#input()
TXT = open('../numb/'+FILELC,'r')
try:
    os.mkdir('../csv')
except:
    pass
CSV = open('../csv/'+FILELC+'.csv','w+',encoding='utf-8')

COLUMNNB = 5#input()
COLUMNLIST = ['序号','X1','X2','X3','Y']

for i in COLUMNLIST:
    CSV.write(i+',')
CSV.write('\n')

TXTLIST = TXT.read().splitlines()
for i in range(len(TXTLIST)):
    try:
        TXTLIST[i] = TXTLIST[i].replace(' ','')
    except:
        pass
print(TXTLIST)
COUNTA = 0
COUNTALIST = []
for o in TXTLIST:
    CSV.write(o+',')
    COUNTA += 1
    if COUNTA % 5 == 0:
        # CSV.write('\n')
        pass
    COUNTALIST.append(COUNTA% 3)
print(COUNTALIST)
CSV.close()
TXT.close()

# print(int('9 08'))