import random
#cteate[0,5,10,12,16]
print("[0,5,10,12,16]")
list1=[True for i in range(0, 3)]
list2=[False for i in range(3, 5)]
list3=[True for i in range(5, 6)]
list4=[False for i in range(6, 10)]
list5=[True]




match_map=[*list1,*list2, *list3,*list4, *list5]
match_map2=[not x for x in match_map]
match_map3=match_map[:-1]
match_map4= [*map(lambda x: True if x%2==0 else False,  [random.randrange(0,10) for i in range(0, 10)])]

def createInterval(match_map):
    print(match_map)
    first_interval_list=[]
    first_width=[]
    second_interval_list=[]
    second_width=[]

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
                first_width.append(count)
                flag=not flag
                count=1
            elif flag==(not match_map[0]):
                if i!=len(match_map)-1:
                    first_interval_list.append(i)
                second_width.append(count)
                flag=not flag
                count=1
        else:
            count+=1

    #second_interval_list=second_interval_list[:-1]
    print(first_interval_list)
    print(first_width)
    print(second_interval_list)
    print(second_width)

createInterval(match_map)
createInterval(match_map2)
createInterval(match_map3)
createInterval(match_map4)