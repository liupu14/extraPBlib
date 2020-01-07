import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set(style="ticks")
plt.rcParams['font.sans_serif'] = ['SimHei']

def jiugonggePlot(x,y,color,namelabel,df):
    x = df['x']
    y = df['y']
    color = df['color']
    namelabel = df['namelabel']
    sns.relplot(x=x,y=y,hue=color,deta=df)
    for ii,jj,zz in zip(x,y,namelabel):
        plt.text(ii,jj,zz,fontsize=8)
    plt.hlines(y=np.percentile(y,33.3),xmin=np.min(x),xmax=np.max(x),colors="red")
    plt.hlines(y=np.percentile(y,66.7),xmin=np.min(x),xmax=np.max(x),colors="red")
    plt.vlines(x=np.percentile(x,33.3),ymin=np.min(y),ymax=np.max(y),colors="red")
    plt.vlines(x=np.percentile(x,66.7),ymin=np.min(y),ymax=np.max(y),colors="red")
    plt.show()

    
    
