import random
from time import sleep
def pr(lis):
    print("*".center(10, "*"))
    print(f"{lis[0]} | {lis[1]} | {lis[2]}")
    print(" ".center(9, " "))
    print(f"{lis[3]} | {lis[4]} | {lis[5]}")
    print(" ".center(9, " "))
    print(f"{lis[6]} | {lis[7]} | {lis[8]}")
def user(lis):
    n = int(input("input number between 1 and 9 :"))
    while n<1 or n>9:
        print("Choose the right choice!!!")
        sleep(1)
        n = int(input("input number between 1 and 9 :"))
    while True:
        if lis[n - 1]!= "-":
            print("Choose another number,bc that is taken")
            n = int(input("input number between 1 and 9 :"))
        else:
            lis[n-1] = "X"
            break
def comp(lis):
    n = random.randint(1,9)
    while lis[n - 1]!= "-":
        n = random.randint(1,9)
    lis[n-1] = "O"
def verify(lis,c):
    ok = False
    for i in range(0,9,3):
        ok = lis[i]==lis[i+1]==lis[i+2]==c
        if ok:
            return ok
    for i in range(0,3):
        ok = lis[i] == lis[i + 3] == lis[i + 6] == c
        if ok:
            return ok
    ok = lis[0] == lis[4] == lis[8] == c
    if ok:
        return ok
    ok = lis[2] == lis[4] == lis[6] == c
    return ok
def completee(lis):
    for x in lis:
        if x=="-":
            return False
    return True
def create():
    print("First state".center(20,"*"))
    lis = ["-" for j in range(9)]
    pr(lis)

    while True:
        user(lis)
        pr(lis)
        if verify(lis, "X"):
            print("You win :)")
            break
        sleep(1)
        comp(lis)
        pr(lis)
        if verify(lis, "O"):
            print("computer wins :(")
            break
        if completee(lis):
            print("Tie")
            break
        sleep(1)
if __name__=="__main__":
    create()

