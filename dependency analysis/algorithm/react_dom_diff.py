class FlagTypes(object):
    Placement="Placement"
    Deletion="Deletion"
    New='New'    

class Node(object):
    def __init__(self, key:str=None, flag:str=None, index:int=None):
        self.key=key
        self.flag=flag
        self.index=index
    def __str__(self):
        return f"key:{self.key}, flag:{self.flag}, index:{self.index}"

a=Node("a")
b=Node("b")
c=Node("c")
d=Node("d")
e=Node("e")
z=Node("z")
y=Node("y")
g=Node("g")
Before=[a, b, c,  e]
After=[a, d, b, c, z, e, y]


def main():

    Last_Placed_Index=0
    Result_List=list()
    Before_Map=dict()

    for index, node in enumerate(Before):
        node.index=index
        Before_Map[node.key]=node

    for i in range(0, len(After)):
        After_Node=After[i]
        After_Node.index=i
        Before_Node=Before_Map.get(After_Node.key, None)

        if(Before_Node !=None):
            del Before_Map[Before_Node.key]
            Old_index=Before_Node.index

            if(Old_index > Last_Placed_Index):
                After_Node.flag=FlagTypes.Placement
                Result_List.append(After_Node)
                continue
            else:
                Last_Placed_Index=Old_index
        else:
            After_Node.flag=FlagTypes.Placement
            Result_List.append(After_Node)

    for i, (key,node) in enumerate(Before_Map.items()):
        node.flag=FlagTypes.New
        Result_List.append(node)

    for result in Result_List:
        print(result)

if __name__=="__main__":

    main()
