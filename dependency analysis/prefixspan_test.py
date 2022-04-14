

WIN10_FILE_NAME_NAME="clean_data_win10.txt"

from prefixspan import PrefixSpan
import random


#Global variables
MIN_RAND_VALUE=3
MAX_RAND_VALUE=10



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
    assert(min_v is not 0)
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
        


#===================================================
#Function Name:
#   Main
#Description:
#   program entry
#===================================================
def main():
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
        if len(pattern[1])>5:
            print(pattern[1])
    

if __name__=="__main__":
    main()