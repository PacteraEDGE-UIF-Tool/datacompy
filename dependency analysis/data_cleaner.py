# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:07:18 2022

@author: cipher kuo
"""

from matplotlib.pyplot import step
import pandas as pd
import re
#helping tool for program bug analysis
from functools import wraps, partial
import numpy as np
import os
import configparser
import functools

#Golbal variable (if __name__==__main__)
filename=r"C:\Users\sheng\experiments\Log Info\DIE_log\DIE_win10_.csv"



def writeInfoToConfig(filename):
    config = configparser.ConfigParser()
    columns_names=pd.read_csv(filename, index_col=0, nrows=0).columns.tolist()
    config['DATA_INFO']={"columns_names":columns_names } 
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def cleanfile(filename,  shared_value_int_for_progressbar:int, outputfloder=str(__file__),):
 #=======================================================================
 #   Returns number of times any function with this decorator is called
 #=======================================================================
    def counter(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            # Call the function being decorated and return the result
            print(wrapper.count)
            return func(*args, **kwargs)
        wrapper.count = 0
        # Return the new decorated function
        return wrapper
    def updateValue():
        nonlocal shared_value_int_for_progressbar
        shared_value_int_for_progressbar.value+=1
        print(shared_value_int_for_progressbar.value)


    class CCounter_with_update_progressbar():
        def __init__(self, func, step_list):
            functools.update_wrapper(self, func)
            self.count=0
            self.step_list=step_list
            self.func = func

        def __call__(self, *args, **kwargs):
            self.count+=1
            #print(self.count)
            if self.count in self.step_list:
                updateValue()
            ret = self.func(*args, **kwargs)
            return ret
    
    writeInfoToConfig(filename)

    log_win10_df=pd.read_csv(filename)
    #select 2 row, all columns
    log_win10_df= log_win10_df.loc[:, ["Prototype", "Result" ]]
    row_number=log_win10_df.shape[0]
    one_step=int(row_number/100)
    step_list=[x for x in range(0, row_number, one_step)]
    print(step_list)
    print(len(step_list))
    real_decorator = partial(CCounter_with_update_progressbar, step_list=step_list)
    @real_decorator
    def regex_map(_string):
        pattern="\s[a-zA-Z]+\("
        m=re.search(pattern, _string, flags=0)
        if  m :
            #drop "(" which is the last character
            return m.group()[:-1]
        else:
            #print("warning! error in regex")
            #print(_string)
            return "NotWindowAPI"



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
    cleanfile(filename, shared_value_int_for_progressbar=0, outputfloder=os.path.dirname(__file__))