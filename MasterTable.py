import numpy as np 
import pandas as pd 

def MergeTable(df1,df2):
    """
    采用笛卡尔方式合并两个数据表
    """
    df1_length = len(df1)
    df2_length = len(df2)
    if df1_length >= df2_length:
        LoopTable = df1 
        BaseTable = df2 
    else:
        LoopTable = df2 
        BaseTable = df1 
    MergeResult = pd.DataFrame()
    Columns = LoopTable.columns 
    for ii in range(len(LoopTable)):
        MediumTable = BaseTable 
        for colname in Columns:
            MediumTable[colname] = LoopTable[colname][ii]
        MergeResult = pd.concat([MergeResult,MediumTable],axis=0)
    return MergeResult 

