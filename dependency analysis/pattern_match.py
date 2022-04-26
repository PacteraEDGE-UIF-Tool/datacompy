
import pickle
import os
import copy
SPLITED_DATA_FOLDER_NAME='splited_dataset'
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


print(len(win10_second_widths), len(win10_first_widths))
print(win10_second_widths[:10])
print(win10_second_interval_list[:10])
print(win10_first_widths[:10])
print(win10_first_interval_list[:10])
'''
new_win10_interval=copy.deepcopy(win10_second_interval_list)
new_win10_widths=copy.deepcopy(win10_second_widths)
for i in range(1, len(win10_second_interval_list)):
    d_value=win10_first_widths[i]-3
    assert(d_value>0)
    new_win10_interval[i]=new_win10_interval[i]-d_value
    new_win10_widths[i]=new_win10_widths[i]+d_value
'''


floder = SPLITED_DATA_FOLDER_NAME
current_path= os.getcwd()
storage_path=os.path.join(current_path, SPLITED_DATA_FOLDER_NAME)
for root, dirs, files in os.walk(floder):
    for file in files:
        os.remove(os.path.join(root, file))


for i in range(1000):
    start= win11_second_interval_list[i]
    length=win11_second_widths[i]
    file_name=str(i)+"_"+"win11_"+str(start)+"_"+str(length)+".txt"
    full_file_path=os.path.join(storage_path, file_name)
    with open(full_file_path, "w+") as f:
        f.write(  "\n".join(  str(item) for item in win11_tokens[start:start+length]))

for i in range(1000):
    start= win10_second_interval_list[i]
    length=win10_second_widths[i]
    file_name=str(i)+"_""win10_"+str(start)+"_"+str(length)+".txt"
    full_file_path=os.path.join(storage_path, file_name)
    with open(full_file_path, "w+") as f:
        f.write(  "\n".join(  str(item) for item in win10_tokens[start:start+length]))
