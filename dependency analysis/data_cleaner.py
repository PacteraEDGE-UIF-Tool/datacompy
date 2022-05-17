# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:07:18 2022

@author: cipher kuo
"""

import pandas as pd
import re
#helping tool for program bug analysis
from functools import wraps
import numpy as np
import os

#Golbal variable
filename=r"C:\Users\sheng\experiments\Log Info\DIE_log\DIE_win10_.csv"
def cleanfile(filename, outputfloder=str(__file__)):
 #=======================================================================
 #   Returns number of times any function with this decorator is called
 #=======================================================================
    def count_check(function, count=[0]):
        @wraps(function)
        def increase_count(*args, **kwargs):
            count[0]  += 1
            print(count[0])
            return function(*args, **kwargs)
        return increase_count


    @count_check
    def regex_map(_string):
        pattern="\s[a-zA-Z]+\("
        m=re.search(pattern, _string, flags=0)
        if  m :
            #drop "(" which is the last character
            return m.group()[:-1]
        else:
            print("warning! error in regex")
            print(_string)
            return "NotWindowAPI"

    log_win10_df=pd.read_csv(filename)
    #select 2 row, all columns
    log_win10_df= log_win10_df.loc[:, ["Prototype", "Result" ]]
    row_number=log_win10_df.shape[0]


    #drop the invalid data
    #log_win10_df.drop(log_win10_df.index[log_win10_df['Prototype'] == "nan"], inplace = True)
    log_win10_df.dropna(axis='rows', inplace=True)
    #filter out the unproper WindowsAPI
    pattern_df = log_win10_df.apply(lambda x:  regex_map(str(x['Prototype'])) +"_"+ str(x['Result']), axis=1)
    #pattern_df.to_csv("output.csv",  index = False)
    #dir=os.path.dirname(filename)
    basefilename=os.path.basename(filename)
    newfilename="cleaned_"+basefilename
    newfilepath_with_name=os.path.join(outputfloder, newfilename)
    with open(newfilepath_with_name, 'w') as f:
        dfAsString = pattern_df.to_string(header=False, index=False)
        f.write(dfAsString)




    '''
    pattern_df = pd.DataFrame(columns=['pattern'])
    for i in range(row_number):
        pattern_string=str(log_win10_df.at[i, "Prototype"])+"_"+ str(log_win10_df.at[i, "Result"])
        pattern_df = pattern_df.append({'pattern': pattern_string}, ignore_index=True)
        
    pattern_df.to_csv("output.csv")
    '''
if __name__=="__main__":
    cleanfile(filename)