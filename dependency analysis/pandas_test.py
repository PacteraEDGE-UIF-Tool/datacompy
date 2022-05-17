
from this import d
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

def exp1():
    lens=15

    data=[i for i in range(lens)]
    datas={'a':data}

    data_left=pd.DataFrame(datas)
    data_right=data_left.copy(deep=True)
    data_left.iloc[3]=77
    data_right.iloc[8]=100
    data_right.iloc[9]=100
    data_right.iloc[10]=100
    print(data_left)
    print(data_right)

    compare = datacompy.Compare(data_left, data_right, join_columns='a')
    compare.matches(ignore_extra_columns=True)
    df1=compare.customized_report()[0]
    df2=compare.customized_report()[1]
    d=compare.customized_report()[2]
    #for idex,row in df1.iterrows():
    #    print(idex)
    print(df1.index)
    l1=list(df1.index)
    print(df2.index)
    print(df2)
    print(d)
def exp2():
    f1="0_win10_0_2930.txt"
    f2="0_win11_0_2900.txt"
    colnames=["whatever"]   
    path="splited_dataset"
    abs_filename1=os.path.join(path, f1)
    abs_filename2=os.path.join(path, f2)
    data_left= pd.read_csv( abs_filename1, delimiter=r'\n',  header=None,names=colnames)
    data_right= pd.read_csv(abs_filename2, delimiter=r'\n',  header=None,names=colnames)
    compare = datacompy.Compare(data_left, data_right, join_columns='whatever')
    compare.matches(ignore_extra_columns=True)
    df1=compare.customized_report()[0]
    #print(df1)
    df1_indexies=df1.index
    df2=compare.customized_report()[1]
    df2_indexies=df2.index
    df3=compare.customized_report()[2]
    #print(df3)
    set1=set()
    list1=list()
    for i in df1_indexies:
        data=df3.loc[i, "whatever"]
        print(data)
        set1.add(data)
    print("==============")
    print(f"set1:{set1}")
    for i in set1:
        print(f"==================================================================={i}")
        tl1=data_left.index[data_left['whatever']==i].tolist()
        for k in tl1:
            print(data_left.loc[k, "whatever"])
        #print(tl1)
        list1=[*list1, *tl1]
    #print(list1)
def exp3():
    f1="1_win10_54_371.txt"
    f2="1_win11_54_367.txt"
    colnames=["whatever"]   
    path="splited_dataset"
    abs_filename1=os.path.join(path, f1)
    abs_filename2=os.path.join(path, f2)
    data1=open( abs_filename1, 'r').read().split("\n")
    data2=open(abs_filename2, 'r').read().split("\n")
    import difflib
    a=difflib.unified_diff(data1, data2, fromfile='file1', tofile='file2', lineterm='')
    for i in a:
        print(i)
exp3()