import numpy as np
import pandas as pd
from pyparsing import col

#GAP <=
#MATCH ⬁



class CSequenceAlignmnt(object):
    def __init__(self, list1:list, list2:list):
        self.list1=list1
        self.list2=list2
        self.solution=list()
        self.solution_path=list()
        self.OptimizeTable=None
        #Define alignment reward
        self.MATCH_REWARD=1
        self.MISMATCH_REWARD=-1
        self.GAP_REWARD=-2

        self.current_col=0
        self.current_row=0
        self.score=0

    def printOPT(self):
        print(r"      ")
        for col_name in self.list2:
            print("%3s" % col_name, end="")
        print("\n")
        for i,row in enumerate(self.OptimizeTable):
            if i==0:
                print(r" ", row)
            else:
                print(self.list1[i-1], row)
    def checkMatch(self):
        if self.list1[self.current_row-1]==self.list2[self.current_col-1]:
            return self.MATCH_REWARD
        else:
            return self.MISMATCH_REWARD

    def getTopValue(self):
        if self.current_col>0:
            return self.OptimizeTable[ self.current_row-1, self.current_col]
    def getLeftValue(self):
        if self.current_col>0:
            print(self.OptimizeTable[self.current_row, self.current_col-1])
            return self.OptimizeTable[self.current_row, self.current_col-1]
    def getDiagonalValue(self):
        if self.current_col>0 and self.current_row >0:
            return self.OptimizeTable[  self.current_row-1,self.current_col-1,]

    def getSolution(self):
        self.current_col=self.list2_len
        self.current_row=self.list1_len
        while(self.current_col>0 and self.current_row>0):
            print(f"col:{ self.current_col}")
            print(f"row: {self.current_row}")
            print(f"value:{self.OptimizeTable[ self.current_row,self.current_col]}")
            DV=self.getDiagonalValue()
            LV=self.getLeftValue()
            TV=self.getTopValue()

            temp_list=[DV, LV, TV]

            best_solution=np.argmax(
                temp_list
            )
            
            if best_solution==0:
                #DiagnalValue is max
                self.solution.append(self.list2[self.current_col-1])
                self.solution_path.append(DV)
                self.current_col-=1
                self.current_row-=1
            elif:
                #LeftValue is max
                self.solution.append(r".")
                self.solution_path.append(LV)
                self.current_col-=1
            else:
                #Top
        



        return self.solution[::-1]
                

    def alignment(self):
        self.list1_len=len(self.list1)
        self.list2_len=len(self.list2)
        OptimizeTable=[[0 for i in range(self.list2_len + 1)] for j in range(self.list1_len + 1)]
        #initialize table
        for row_index in range(1, self.list1_len + 1):
            OptimizeTable[row_index][0] = row_index * (-2)

        for col_index in range(1, self.list2_len +1):
            OptimizeTable[0][col_index]= col_index * (-2)


        self.OptimizeTable=np.matrix(OptimizeTable)
        self.printOPT()

        for row_index in range(1, self.list1_len+1):
            for col_index in  range(1, self.list2_len+1):
                print(f"row {row_index}, col {col_index}")
                self.current_col=col_index
                self.current_row=row_index
                self.OptimizeTable[ row_index, col_index,]=max(
                    self.getTopValue() + self.GAP_REWARD,
                    self.getLeftValue()+self.GAP_REWARD,
                    self.getDiagonalValue()+self.checkMatch()
                )
                self.printOPT()
        

        self.printOPT()


        '''
        for col_index in range(1, self.list1 + 1):
            for row_index in range(1, self.list2 + 1):
                self.OptimizeTable[col_index][row_index] = min(
                    self.OptimizeTable[i - 1][j - 1] + self.delta(self.x, self.y, i - 1, j - 1),
                    OPT[i - 1][j] + 1,
                    OPT[i][j - 1] + 1,
                )
        '''
z5=["0" for i in range(50)]
o3=["1" for i in range(30)]

z5_1=["0" for i in range(49)]
o3_1=["1" for i in range(29)]

l1=[*z5, *o3]
l2=[*z5_1, "1","0",*o3_1]


seq=CSequenceAlignmnt(l1, l2)
seq.alignment()
seq.getSolution()
print(l1)
print(l2)
print(seq.solution[::-1])
print(seq.solution_path)



    
