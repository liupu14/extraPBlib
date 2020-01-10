import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set(style="ticks")
plt.rcParams['font.sans_serif'] = ['SimHei']

def jiugonggePlot(x,y,color,namelabel,ways="abs",df):
    x = df['x']
    y = df['y']
    color = df['color']
    namelabel = df['namelabel']
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)
    x_ld = (x_min + (x_max - x_min)/3) if ways=="abs" else np.percentile(x,33.3)
    x_ud = (x_max - (x_max - x_min)/3) if ways=="abs" else np.percentile(x,66.7)
    y_ld = (y_min + (y_max - y_min)/3) if ways=="abs" else np.percentile(y,33.3)
    y_ud = (y_min + (y_max - y_min)/3) if ways=="abs" else np.percentile(y,66.7)
    sns.relplot(x=x,y=y,hue=color,data=df)
    for ii,jj,zz in zip(x,y,namelabel):
        plt.text(ii,jj,zz,fontsize=8)
    plt.hlines(y=y_ld,xmin=x_min,xmax=x_max,colors="red")
    plt.hlines(y=y_ud,xmin=x_min,xmax=x_max,colors="red")
    plt.vlines(x=x_ld,ymin=y_min,ymax=y_max,colors="red")
    plt.vlines(x=x_ld,ymin=y_min,ymax=y_max,colors="red")
    plt.show()

    
    
