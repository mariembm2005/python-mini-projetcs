from random import randint
M = [[' ' for i in range(10)] for j in range(10)]
def affich():
    for i in range(10):
        print("[",end="")
        for j in range(10):
            print(M[i][j].rjust(3),end="")
        print("]")
def remplir():
    print("**************")
    for i in range(30):
        x = (randint(0, 9), randint(0, 9))
        x = list(x)
        while(M[x[0]][x[1]] == "X"):
            x = (randint(0, 9), randint(0, 9))
        M[x[0]][x[1]] = "X"
def one(r,c,ch):
    ok = False
    c1 = 0 if c-1<=0 else c-1
    r1 = 0 if r - 1 <=0 else r-1
    for i in range(r1,r+2):
        for j in range(c1,c+2):
            if i==r and j==c:
                continue
            elif (i > 9 or i < 0) or (j > 9 or j < 0):
                continue
            if M[i][j]=="X" or M[i][j]!=" ":
                continue
            M[i][j] = ch
            ok = True
    return ok


affich()
remplir()
affich()
while True:
    o = input("Input the position of 0: ").split(",")
    p1 = int(o[0])
    p2 = int(o[1])
    if M[p1][p2] == "X":
        continue
    else:
        break
M[p1][p2] = "0"
print("**************")
affich()
one(p1,p2,"1")
print("**************")
affich()
n = 1
ch = 2
print("**************")
while True:
    ok = False
    for i in range(10):
        for j in range(10):
            if M[i][j]==str(ch-1):
                if one(i,j,str(ch)):
                    ok = True

    if not ok:
        break
    print("**************")
    affich()


    ch+=1





