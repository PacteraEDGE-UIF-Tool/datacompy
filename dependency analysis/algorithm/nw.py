

class SequenceAlignment(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.solution = []

    delta = lambda self, x, y, i, j: 1 if x[i] != y[j] else 0

    def find_solution(self, OPT, m, n):
        if m == 0 and n == 0:
            return

        # We can only do insert if n != 0, align if there are element in both x, y, etc.
        insert = OPT[m][n - 1] + 1 if n != 0 else float("inf")
        align = (
            OPT[m - 1][n - 1] + self.delta(self.x, self.y, m - 1, n - 1)
            if m != 0 and n != 0
            else float("inf")
        )
        delete = OPT[m - 1][n] + 1 if m != 0 else float("inf")

        best_choice = min(insert, align, delete)

        if best_choice == insert:
            self.solution.append("insert_" + str(self.y[n - 1]))
            return self.find_solution(OPT, m, n - 1)

        elif best_choice == align:
            self.solution.append("align_" + str(self.y[n - 1]))
            return self.find_solution(OPT, m - 1, n - 1)

        elif best_choice == delete:
            self.solution.append("remove_" + str(self.x[m - 1]))
            return self.find_solution(OPT, m - 1, n)

    def alignment(self):
        n = len(self.y)
        m = len(self.x)
        OPT = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1, m + 1):
            OPT[i][0] = i

        for j in range(1, n + 1):
            OPT[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                OPT[i][j] = min(
                    OPT[i - 1][j - 1] + self.delta(self.x, self.y, i - 1, j - 1),
                    OPT[i - 1][j] + 1,
                    OPT[i][j - 1] + 1,
                )  # align, delete, insert respectively

        self.find_solution(OPT, m, n)

        return (OPT[m][n], self.solution[::-1])

#l1=["A","B","A","D"]
#l2=["A","B","A","C","C","D"]
z5=["0" for i in range(50)]
o3=["1" for i in range(30)]

z5_1=["0" for i in range(49)]
o3_1=["1" for i in range(29)]

l1=[*z5, *o3]
l2=[*z5_1, "1","0",*o3_1]

seq=SequenceAlignment(l1, l2)
print(seq.alignment())