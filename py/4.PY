#导入包
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
# %matplotlib inline
from pickle import LIST
import matplotlib.pylab as plb
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
LISTA = [126, 149, 143, 141, 127, 123, 137, 132, 135, 134, 146, 142, 135, 141, 150, 137, 144, 137, 134, 139, 148, 144, 142, 137, 147, 138, 140, 132, 149, 131, 139, 142, 138, 145, 147, 137, 135, 142, 151, 146, 129, 120, 143, 145, 142, 136, 147, 128, 142, 132, 138, 139, 147, 128, 139, 146, 139, 131, 138, 149];

p1 = plt.hist(LISTA,10,density = True,color='#444693',alpha = 0.5)

df = pd.DataFrame(LISTA,columns = ['height'])
#读入数据
# fname = r"F:\文章\数据挖掘概念与技术\第2章\Qo图\studentsPerformance.csv"df = pd .read_csv(fname , engine=" python " )
# df = df.loc[ : , [ 'math score ' , ' reading score ' , ' writing score']]#求总分数
# df [ 'score_tol' ] = df[ 'math score']+df[ 'reading score' ]+ df[ 'writing score']
#舷照总戍绩排序
df = df.sort_values('height' ,ascending=False).reset_index(drop=True)#计算舷照成籁得到的分位数
df[ '分位数']= df[ 'height' ].rank(pct=True ,ascending=False)
#调包画oQ图―猃验是否符合正态分布
stats.probplot(df[ 'height'], dist="norm" , plot=plt)
plt.show( )
