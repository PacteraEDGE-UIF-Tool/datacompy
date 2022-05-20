
from compileall import compile_path
import pickle
import os
import copy
import collections
import sqlite3
import sys
import traceback
import hashlib
import pickle
import json

from matplotlib.pyplot import connect
SPLITED_DATA_FOLDER_NAME='splited_dataset'
PATTERN_DATA_FOLDER_NAME='patterns_dataset'
DATABASE="Sqlite3.db"


def get_ith_pattern(i, interval_list, width_list, tokens):
    pattern_start=interval_list[i]
    pattern_width=width_list[i]
    pattern_end=pattern_start+pattern_width
    pattern=tokens[pattern_start+i: pattern_end]
    return pattern



def createUnMatchPatternHashTable1(_connection):
        #Create Sqlite table
    cursor=_connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Optimize_pattern_first(
                Hash_of_patterns TEXT PRIMARY KEY,
                Patterns TEXT,
                Index_of_pattern INT
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

def createUnMatchPatternHashTable2(_connection):
        #Create Sqlite table
    cursor=_connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Optimize_pattern_second(
                Hash_of_patterns TEXT PRIMARY KEY,
                Patterns TEXT,
                Index_of_pattern INT
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

def md5hash(string:str):
    md5 = hashlib.md5()
    encodestring=string.encode("utf-8")
    md5.update(encodestring)
    return md5.hexdigest()
      
def insertDataIntoDB(_connection, patterns, index, first_or_second):
    assert(first_or_second=="first" or first_or_second=="second")
    cursor=_connection.cursor()  
    concat_patterns=(" ").join(patterns)
    hash_of_pattern=md5hash(concat_patterns)
    SQL_INSERT_DATA_SRT=f"""
    INSERT INTO {"Optimize_pattern_"+first_or_second} (
                Hash_of_patterns TEXT PRIMARY KEY,
                Patterns TEXT,
                Index_of_pattern INT VALUES(
        \'{hash_of_pattern}\',
        \'{concat_patterns}\'
        \'{index}\'
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


DATASET_PATH=r"C:\Users\sheng\experiments\Log_analysis\dependency analysis"
WIN10_FILE_NAME=r"cleaned_data_win10.txt"
WIN11_FILE_NAME=r"cleaned_data_win11.txt"
win10data=None
win10_file_path=os.path.join(DATASET_PATH, WIN10_FILE_NAME)
win10data=open(win10_file_path, 'r', encoding='utf-8').read()
assert(win10data is not None)


win11data=None
win11_file_path=os.path.join(DATASET_PATH, WIN11_FILE_NAME)
win11data=open(win11_file_path,'r', encoding='utf-8').read()


#create tokens
win10_tokens=win10data.split()
win11_tokens=win11data.split()

win11_first_interval_list=None
win11_first_widths=None
win11_second_interval_list=None
win11_second_widths=None

win10_first_interval_list=None
win10_first_widths=None
win10_second_interval_list=None
win10_second_widths=None

with  open ('win11_first_interval_list.pickle', 'rb') as fp:
    win11_first_interval_list = pickle.load(fp)

with open('win11_first_widths.pickle','rb') as fp:
    win11_first_widths=pickle.load(fp)

with  open ('win11_second_interval_list.pickle', 'rb') as fp:
    win11_second_interval_list = pickle.load(fp)

with open('win11_second_widths.pickle','rb') as fp:
    win11_second_widths=pickle.load(fp)

with  open ('win10_first_interval_list.pickle', 'rb') as fp:
    win10_first_interval_list = pickle.load(fp)

with  open ('win10_second_interval_list.pickle', 'rb') as fp:
    win10_second_interval_list = pickle.load(fp)

with open('win10_second_widths.pickle','rb') as fp:
    win10_second_widths=pickle.load(fp)

with open('win10_first_widths.pickle','rb') as fp:
    win10_first_widths=pickle.load(fp)


max_len=min(len(win10_first_widths), len(win11_first_widths))


#try to match the interval range
Flag=False
for i, value in enumerate(win10_first_widths):
    if i==max_len:
        break
    if win11_first_widths[i]!=value:
        print(f"index :{i}, value:{value}")
        print(f"win11: {win11_first_widths[i]}")
        win11_start=win11_first_interval_list[i]
        win11_end=win11_start+win11_first_widths[i]
        win11_match_tokens=win11_tokens[win11_start:win11_end]
        win10_start=win10_first_interval_list[i]
        win10_end=win10_start+win10_first_widths[i]
        print(f"win10_end:{win10_end}")
        win11_pattern=win11_tokens[win11_start: win11_end]
        #print(win11_start)
        win10_pattern=win10_tokens[win10_start:win10_end]
        #print(win10_start)
        #print(win11_pattern)
        #print(win10_pattern)
        #check first 3 token

        for i in range(0,3):
            if win11_tokens[win11_start+i: win11_start+i] !=win10_tokens[win10_start+i: win10_start+i]:
                Flag=True
    if  Flag:
        print(f"{win11_tokens[win11_start+i: win11_end]}: {win10_tokens[win10_start+i: win10_end]}")
        break           

'''
print(len(win10_second_widths), len(win10_first_widths))
print(win10_second_widths[:10])
print(win10_second_interval_list[:10])
print(win10_first_widths[:10])
print(win10_first_interval_list[:10])
print(win11_second_widths[:10])
print(win11_second_interval_list[:10])
print(win11_first_widths[:10])
print(win11_first_interval_list[:10])
'''
connection=sqlite3.connect(DATABASE)
createUnMatchPatternHashTable1(connection)
createUnMatchPatternHashTable2(connection)

#first = pattern
win11_patterns_hash_dict=dict()
unmatch_list=[]
for i, pattern_width in enumerate(win11_first_widths):
    win10_pattern=get_ith_pattern(i, win10_first_interval_list, win10_first_widths, win10_tokens)
    win11_pattern=get_ith_pattern(i, win11_first_interval_list, win11_first_widths, win11_tokens)
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    comp_result=compare(win10_pattern, win11_pattern)
    #no matter what win11 pattern is, store it into database
    insertDataIntoDB(connection, win11_pattern, i, "second")
    if comp_result==False:
        print(i)
        #insert unmatch win10 pattern into database
        insertDataIntoDB(connection, win10_pattern, i, "first")
        unmatch_list.push( md5hash((" ").joi(win10_pattern)))
for unmatch_hash in unmatch_list:
    #try to find the 






#generate files
floder = SPLITED_DATA_FOLDER_NAME
current_path= os.getcwd()
storage_path=os.path.join(current_path, SPLITED_DATA_FOLDER_NAME)
for root, dirs, files in os.walk(floder):
    for file in files:
        os.remove(os.path.join(root, file))

floder = PATTERN_DATA_FOLDER_NAME
current_path= os.getcwd()
patterns_path=os.path.join(current_path,  PATTERN_DATA_FOLDER_NAME)
for root, dirs, files in os.walk(floder):
    for file in files:
        os.remove(os.path.join(root, file))

number=min(len(win10_second_interval_list), len(win11_second_interval_list))
#gen unmatch datas
for i in range(number):
    start= win11_second_interval_list[i]
    length=win11_second_widths[i]
    file_name=str(i)+"_"+"win11_"+str(start)+"_"+str(length)+".txt"
    full_file_path=os.path.join(storage_path, file_name)
    with open(full_file_path, "w+") as f:
        f.write(  "\n".join(  str(item) for item in win11_tokens[start:start+length]))

for i in range(number):
    start= win10_second_interval_list[i]
    length=win10_second_widths[i]
    file_name=str(i)+"_""win10_"+str(start)+"_"+str(length)+".txt"
    full_file_path=os.path.join(storage_path, file_name)
    with open(full_file_path, "w+") as f:
        f.write(  "\n".join(  str(item) for item in win10_tokens[start:start+length]))

#gen patterns
for i in range(number):
    start= win11_first_interval_list[i]
    length=win11_first_widths[i]
    file_name=str(i)+"_Patterns"+"_"+"win11_"+str(start)+"_"+str(length)+".txt"
    full_file_path=os.path.join(patterns_path, file_name)
    with open(full_file_path, "w+") as f:
        f.write(  "\n".join(  str(item) for item in win11_tokens[start:start+length]))

for i in range(number):
    start= win10_first_interval_list[i]
    length=win10_first_widths[i]
    file_name=str(i)+"_Patterns"+"_""win10_"+str(start)+"_"+str(length)+".txt"
    full_file_path=os.path.join(patterns_path, file_name)
    with open(full_file_path, "w+") as f:
        f.write(  "\n".join(  str(item) for item in win10_tokens[start:start+length]))
