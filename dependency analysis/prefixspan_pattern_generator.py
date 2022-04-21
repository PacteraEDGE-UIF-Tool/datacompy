

from encodings import search_function
from enum import unique
from re import S
from prefixspan import PrefixSpan
import random
import sqlite3
import traceback
import sys
import os
import hashlib

import numpy as np
from matplotlib import colors as mcolors 
import matplotlib.pyplot as plt




#Global variables


WIN10_FILE_NAME=r"E:\experiments\Log_analysis\dependency analysis\cleaned_data_win10.txt"
WIN11_FILE_NAME=r"E:\experiments\Log_analysis\dependency analysis\cleaned_data_win10.txt"
MIN_RAND_VALUE=2
MAX_RAND_VALUE=10
#the minum threshold for pattern appear time
PATTERN_NUMBER_THRESHOLD=5
DATABASE="Sqlite3.db"
filtered_pattern_list=[]
first_pattern_list=[]



'''
Description

'''
def matchIndexAndPattern(_indexies:int, _patterns:str, _tokens):
    first_pattern=_patterns[0]
    result_list=[]
    for index in _indexies:
        allmatchflag=1
        for i in range(0, len(_patterns)):
            if index+len(_patterns) <len(_tokens):
                if _tokens[index+i]!=_patterns[i]:
                    allmatchflag=0
                    break
            else:
                break
        if allmatchflag ==1:
            result_list.append(index)
            allmatchflag=1
    return result_list

'''

Description:
    create a dictionary that we are able to find all of
    the positions of certaint pattern 

'''
def createIndexDictionary(tokens):
    index_dictionary=dict()
    indexies=[x for x in range(0, len(tokens))]
    token_index_pairs=zip(tokens, indexies)
    for pair in token_index_pairs:
        (token, index)=pair
        if token not in index_dictionary:
            index_dictionary[token]= list()
            index_dictionary[token].append(index)
        else:
            index_dictionary[token].append(index)
    return index_dictionary

'''


'''
def createIntervalList(match_map):
    print(match_map)
    first_interval_list=[]
    first_widths=[]
    second_interval_list=[]
    second_widths=[]

    #append diff flag in the end of map,
    #so for loop will know when to stop

    match_map.append(not match_map[-1])

    flag=match_map[0]
    first_interval_list.append(0)#start from 0


    count=0
    for i in range(0, len(match_map)):
        #there are two conditions while match_map[i] meet differen flag, flag=match_map[0], or not match_map[0]
        if match_map[i] !=flag:
            if flag==match_map[0]:
                if i !=len(match_map)-1:
                    second_interval_list.append(i)
                first_widths.append(count)
                flag=not flag
                count=1
            elif flag==(not match_map[0]):
                if i!=len(match_map)-1:
                    first_interval_list.append(i)
                second_widths.append(count)
                flag=not flag
                count=1
        else:
            count+=1
    return first_interval_list, first_widths, second_interval_list, second_widths
'''
Function Name: 
    create_random_number_range_seqence_lenth_generator(min_v, max_v, token_number)
Return type:
   list
Description:
   generate a list that contain with the random number between min
   and max value, the summation of those value should be 'token_number'.
example:
   func(1,5, 20) =>[1,2,3,4,1,2,3,4]
'''
def create_random_number_range_seqence_lenth_generator(min_v, max_v, token_number):
    assert(min_v > 0)
    assert(max_v < token_number)
    rand_list=[]
    total_number=token_number
    while(total_number>0):
        rand_value=random.randrange(min_v, max_v)
        total_number-=rand_value
        if(total_number<0):
            rand_list.append(0-total_number)
        else:
            rand_list.append(rand_value)
    #assert(sum(rand_list)== token_number)
    print(sum(rand_list))
    print(token_number)
    return rand_list



'''
Function Name:
   gen_2d_array_with_rand_list(tokens, rand_list)
Return Type:
    2d array [[]]
Description:
    generate 2d array according to rand_list
'''
def gen_2d_array_with_rand_list(tokens, rand_list):
    two_d_array=[]
    array=[]
    count=0
    for rand_val in rand_list:
        array.extend(tokens[count:count+rand_val])
        two_d_array.append(array)
        array=[]
        count+=rand_val
    return two_d_array



'''
Function Name:
    dropDuplicatePatterns(_connection, _first_pattern):
Description:
    drop duplicate pattern, and remain the max or minum length sequtail pattern,
    remain the minum-length one might make sence.

    return the hash_list, which have dropped the duplicate start with first pattern
'''
def dropDuplicatePatterns(_connection, _first_pattern):
    #print(first_pattern)
    Result_hash_list=[]
    hash_UniqueSEQ_and_SEQ_LEN_dict=dict()
    hash_UniqueSEQ_and_hash_OriginSEQ_dict=dict()
    cursor=_connection.cursor()
    try:
        cursor.execute(f"""
            SELECT 
            Hash_of_original_sequential_patterns,
            Hash_of_unique_sequential_patterns,
            Sequence_length
            from  pattern_info
            WHERE First_pattern = \'{_first_pattern}\'
        ;
        """)
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        _connection.close()
    rows=cursor.fetchall()
    if len(rows) <2:
        print(f"{_first_pattern} len(unique_pattern)< 2, add into result hash list")
    for row in rows:
        #print(row)
        (hash_of_original_seq, hash_of_unique_pattern,  seq_length)=row
        if hash_of_unique_pattern in hash_UniqueSEQ_and_SEQ_LEN_dict:
            #keep the min(length, oldlength)
            #if old len > new len
            #==========================================================================
            # less than greater than is very important, change the symbol here
            #==========================================================================
            if hash_UniqueSEQ_and_SEQ_LEN_dict[hash_of_unique_pattern]> seq_length:
                Old_hash=hash_UniqueSEQ_and_hash_OriginSEQ_dict[hash_of_unique_pattern]
                #remove the old hash 
                Result_hash_list.remove(Old_hash) 
                # and append new hash
                Result_hash_list.append(hash_of_original_seq)
                #update the length dict
                hash_UniqueSEQ_and_SEQ_LEN_dict[hash_of_unique_pattern]=seq_length
        else:
            #add info into dictionary
            hash_UniqueSEQ_and_SEQ_LEN_dict[hash_of_unique_pattern]=seq_length
            hash_UniqueSEQ_and_hash_OriginSEQ_dict[hash_of_unique_pattern]=hash_of_original_seq
            Result_hash_list.append(hash_of_original_seq)
    return Result_hash_list


def md5hash(string:str):
    md5 = hashlib.md5()
    encodestring=string.encode("utf-8")
    md5.update(encodestring)
    return md5.hexdigest()

'''
#Function Name:
'''
def insertDataIntoDB(_connection, _sequential_patterns):
    
    cursor=_connection.cursor()
    the_concatted_sequential_pattern=(" ").join(_sequential_patterns)
    hash_value=md5hash(the_concatted_sequential_pattern)

    sequence_length=len(_sequential_patterns)

    first_pattern=_sequential_patterns[0]
    if first_pattern not in first_pattern_list:
        first_pattern_list.append(first_pattern)

    unique_set=[]
    for pattern in _sequential_patterns:
        if pattern not in unique_set:
            unique_set.append(pattern)

    concatted_unique_sequential_pattern=((" ").join(unique_set))     
    hash_of_unique_set_value=md5hash(concatted_unique_sequential_pattern)

    concatted_original_sequential_pattern=(" ").join(_sequential_patterns)
    #print(f"{first_pattern} : {concatted_unique_sequential_pattern} :{hash_value}")
    SQL_INSERT_DATA_SRT=f"""
    INSERT INTO pattern_info (
        Hash_of_original_sequential_patterns,
        Hash_of_unique_sequential_patterns,
        Sequence_length,
        First_pattern,
        Unique_sequential_pattern,
        Original_sequential_pattern) VALUES(
        \'{hash_value}\',
        \'{hash_of_unique_set_value}\',
        {sequence_length},
        \'{first_pattern}\',
        \'{concatted_unique_sequential_pattern}\',
        \'{concatted_original_sequential_pattern}\'
        );
        """
    #print(SQL_INSERT_DATA_SRT)
    try:
        cursor.execute(SQL_INSERT_DATA_SRT)
        _connection.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        _connection.close()

'''
FunctionName

'''
def createPatternInfoTable(_connection):
        #Create Sqlite table
    cursor=_connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pattern_info(
                Hash_of_original_sequential_patterns TEXT PRIMARY KEY,
                Hash_of_unique_sequential_patterns TEXT,
                Sequence_length INTEGER,
                First_pattern TEXT,
                Unique_sequential_pattern  TEXT,
                Original_sequential_pattern TEXT
            );
        """)
        _connection.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        _connection.close()
'''


'''
def getTheOriginalPatternFromHash(_connection, _Result_hash):
    cursor=_connection.cursor()
    Result_Original_Patterns_list=[]
    try:
        cursor.execute(f"""
        SELECT Original_sequential_pattern from pattern_info
        WHERE Hash_of_original_sequential_patterns= \'{_Result_hash}\'
        ;
        """)
        _connection.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        _connection.close()
    rows=cursor.fetchone()
    for row in rows:
        Result_Original_Patterns_list.append(row)
    return Result_Original_Patterns_list


'''
#Function Name:


#Description:
     Visualize the result

'''
def visualizeResult(match_interval_start, match_width_list, unmatch_interval_start, unmatch_width_list):
                     
    #column_name_set=["unmatch","match","reserve"]
    column_names=["match","unmatch"]

    labels=["win10"]

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, max(match_interval_start))

    color1="#00FFFF"
    color2="#00008B"
    rects = ax.barh(labels, match_width_list, left=match_interval_start, height=0.1,
        label="match", color=color1)
    rects = ax.barh(labels, unmatch_width_list, left=unmatch_interval_start, height=0.1,
        label="unmatch", color=color2)
    '''
        #show text on the bar
        text_color = 'white'
        ax.bar_label(rects, label_type='center', color=text_color)
    '''

    ax.legend(ncol=len(column_names), bbox_to_anchor=(0, 1),
                loc='lower left', fontsize='small')
    plt.show() 



'''
#Description:
    #Why we need match map? not just return the range?, because the interval can be merged,
    #.e.g    [2,1] mean index 2 with 1 length pattern match, but there might have [1,3] 
'''
def createMatchMap(Result_patterns_list, index_dictionary, tokens):

    match_pattern_indexies_range_list=list()
    match_map=[False for i in range(0,len(tokens))]
    assert(len(match_map)==len(tokens))

    for patterns in Result_patterns_list:
        patterns_len=len(patterns)
        #use the first pattern of paterns to look up dictionary.
        indexies=index_dictionary[patterns[0]]
        result_match_list=matchIndexAndPattern(indexies, patterns, tokens)
        for result_index in result_match_list:
            match_pattern_indexies_range_list.append((result_index, patterns_len))
    for from_to_tupple in match_pattern_indexies_range_list:
        (index_from, patterns_len) = from_to_tupple
        if index_from + patterns_len < len(tokens):
            for i in range(0, patterns_len):
                #print(index_from, patterns_len)
                match_map[index_from+i]=True
    return match_map
#===================================================
#Function Name:
#   Main
#Description:
#   program entry
#===================================================
def main():

    Result_hash_list=[]
    Result_pattern_list=[]

    if os.path.isfile(DATABASE):
        os.remove(DATABASE)


    connection=sqlite3.connect(DATABASE)
    cursor=connection.cursor()
    
    
    
    #read data
    win10data=None
    win10data=open(WIN10_FILE_NAME, 'r', encoding='utf-8').read()
    assert(win10data is not None)


    win11data=None
    win11data=open(WIN11_FILE_NAME,'r', encoding='utf-8').read()


    #create tokens
    tokens=win10data.split()
    win11_tokens=win11data.split()


    #create dictionary return a python dictionary in following form dic{"first_pattern":[1,100,1000...],second_pattern}
    win11_index_dictionary=createIndexDictionary(win11_tokens)
    index_dictionary=createIndexDictionary(tokens)


    

    tokens_num=len(tokens)
    win11_tokens_num=len(win11_tokens)


    #need to transform the data into two dimention array.
    rand_list=create_random_number_range_seqence_lenth_generator(MIN_RAND_VALUE, MAX_RAND_VALUE, tokens_num)
    data_array=gen_2d_array_with_rand_list(tokens, rand_list)
    
    #print(data_array[:10])
    ps = PrefixSpan(data_array)

    '''
    For both frequentcy and top-k algorithms, a custom key function key=lambda patt, matches: ... can be applied,
    where pattern is the current pattern and matches is the current list of matching sequence (id, position) tuples.
    '''
    patterns=ps.topk(6000)
    for pattern in patterns:
        #pattern in the form like (24794, ['TlsGetValue_OK'])
        #if the pattern length> threshold then push it into list
        #.e.g ['a','b','a','c'] pattern length=4
        if len(pattern[1])>PATTERN_NUMBER_THRESHOLD:
            filtered_pattern_list.append(pattern[1])

    #create the data base table
    createPatternInfoTable(connection)

    #store the first element in pattern
    #sequential pattern in the following format
    # .e.g ['CallNextHookEx_OK', 'PeekMessageW_OK', 'DispatchMessageW_*', 'TlsGetValue_OK', 'GetWindowLongW_*', 'GetWindowLongW_OK']
    print(len(filtered_pattern_list))
    for sequential_patterns in filtered_pattern_list:
        insertDataIntoDB(connection, sequential_patterns)

    #drop duplicate pattern
    for first_pattern in first_pattern_list:
        _Result_hash_list=dropDuplicatePatterns(connection, first_pattern)
        Result_hash_list.extend(_Result_hash_list)

    print(Result_hash_list)

    for Result_hash in Result_hash_list:
        Result_pattern_list.append(getTheOriginalPatternFromHash(connection, Result_hash))
    
    #print(Result_pattern_list)
    print(len(Result_pattern_list))
    #from string to splited object .e.g: [["1 2 3 4"],["5 6 7 8"]] =>[["1","2","3","4"],["5","6","7","8"]]
    Result_pattern_list=[Result_pattern[0].split(" ") for Result_pattern in Result_pattern_list]
    #sort the list, by the first element of each sub-list
    Result_patterns_list= sorted(Result_pattern_list, key=lambda x: x[0])
    print(Result_patterns_list)


    
    #Create match map
    win10_match_map=createMatchMap(Result_patterns_list, index_dictionary, tokens)
    #Use win10 pattern to create the match map for win11
        
    first_interval_list, first_widths, second_interval_list, second_widths=createIntervalList(win10_match_map)
    visualizeResult(first_interval_list, first_widths, second_interval_list, second_widths)
    '''
    patterns_1=Result_patterns_list[0]
    indexies=index_dictionary[patterns_1[0]]
    result_match_list=matchIndexAndPattern(indexies, patterns_1, tokens)
    print(f"target pattern:{patterns_1}")
    for i in result_match_list:
        print(i)               
        print(tokens[i:i+len(patterns_1)])
    print(tokens[286542:286576])
    '''
if __name__=="__main__":
    main()