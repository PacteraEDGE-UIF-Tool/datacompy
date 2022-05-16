from doctest import OutputChecker
import pandas as pd
import os
import glob
import datacompy
from pure_eval import group_expressions


OutputFloder="./splited_dataset"

file_name_left=os.path.join(OutputFloder, str(251)+"_win10*")
file_name_right=os.path.join(OutputFloder, str(251)+"_win11*")
colnames=["whatever"]
#=====================
#data_left= pd.read_csv(glob.glob(file_name_left)[0], delimiter=r'\n',  header=None,names=colnames)
#data_left.index = [x for x in range(1, len(data_left.values)+1)]
#data_left.index.whatever='id'
#=======================
#data_right= pd.read_csv(glob.glob(file_name_right)[0], delimiter=r'\n',  header=None,names=colnames)
#data_right.index=[x for x in range(1, len(data_right.values)+1)]


lens=15

data=[i for i in range(lens)]
datas={'a':data}

data_left=pd.DataFrame(datas)
data_right=data_left.copy(deep=True)
data_right.iloc[8]=100
data_right.iloc[10]=100
print(data_left)
print(data_right)

compare = datacompy.Compare(data_left, data_right, join_columns='a')
compare.matches(ignore_extra_columns=False)
df1=compare.customized_report()[0]
#for idex,row in df1.iterrows():
#    print(idex)
print(df1.index)
l1=list(df1.index)
print(l1)