

WIN10_FILE_NAME_NAME="clean_data_win10.txt"

from re import S
from prefixspan import PrefixSpan
import random


#Global variables
MIN_RAND_VALUE=3
MAX_RAND_VALUE=10
PATTERN_NUMBER_THRESHOLD=5


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
#Function Name:

'''

#===================================================
#Function Name:
#   Main
#Description:
#   program entry
#===================================================
def main():


    filtered_pattern_list=[]



    data=None
    data=open(WIN10_FILE_NAME_NAME, 'r', encoding='utf-8').read()
    assert(data is not None)

    tokens=data.split()
    tokens_num=len(tokens)
    #need to transform the data into two dimention array.
    rand_list=create_random_number_range_seqence_lenth_generator(MIN_RAND_VALUE, MAX_RAND_VALUE, tokens_num)
    
    data_array=gen_2d_array_with_rand_list(tokens, rand_list)
    
    
    #print(data_array[:10])
    ps = PrefixSpan(data_array)

    '''
    For both frequent and top-k algorithms, a custom key function key=lambda patt, matches: ... can be applied,
    where patt is the current pattern and matches is the current list of matching sequence (id, position) tuples.
    '''
    patterns=ps.topk(6000)
    for pattern in patterns:
        #pattern in the form like (24794, ['TlsGetValue_OK'])
        #if the pattern length> threshold then push it into list
        #.e.g ['a','b','a','c'] pattern length=4
        if len(pattern[1])>PATTERN_NUMBER_THRESHOLD:
            filtered_pattern_list.append(pattern[1])

    #store the first element in pattern
    # .e.g ['CallNextHookEx_OK', 'PeekMessageW_OK', 'DispatchMessageW_*', 'TlsGetValue_OK', 'GetWindowLongW_*', 'GetWindowLongW_OK']
    for sequential_patterns in filtered_pattern_list:
        if  sequential_patterns[0]

    keys_list=dict()
    



if __name__=="__main__":
    main()