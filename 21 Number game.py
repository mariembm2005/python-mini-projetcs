import random
lis = []
n = len(lis)
def lose1():
    print ("\nYOU LOSE !")
    print("Better luck next time !")
def check(xyz):
    return all(xyz[i] - xyz[i - 1] == 1 for i in range(1, len(xyz)))
def user(lis):
    print("Your turn.")
    count = int(input("How many numbers do you wish to enter?  "))
    if count not in [1,2,3]:
        print("Invalid choice! You can only enter 1, 2, or 3 numbers.")
        return user(lis)
    for i in range(count):
        x = int(input(">"))
        if x != lis[-1] + 1:
            print("Wrong number! You must follow the sequence.")
            return user(lis)
        lis.append(x)
        if lis[-1]==20:
            print("You Won!!!!")
def comp(lis):
    n = len(lis)-1
    for i in range(1,random.randint(2,4)):
        n+=1
        lis.append(n)
        if lis[-1] == 20:
            lose1()
            break
    print(f"Order of inputs after computer's turn is: {lis}")


def start1(lis):
    su = 0
    sc = 0
    if input("Enter 'F' to take the first chance.Enter 'S' to take the second chance :\n> ").lower() == 'f':
        user(lis)
        su += 1
    else:
        comp(lis)
        sc += 1

    while True:
        if su > sc:
            comp(lis)
            sc += 1
        else:
            user(lis)
            su += 1
        if lis[-1]==20:
            break
def main():
    while True:
        ch = input("Do you want to start the game? (Yes/No) : ")
        if ch.lower()=="yes":
            lis = [0]
            start1(lis)
        else:
            print("Do you want quit the game?(yes / no)")
            nex = input('> ')
            if nex == "yes":
                print("You are quitting the game...")
                exit(0)
            elif nex == "no":
                print("Continuing...")
            else:
                print("Wrong choice")
if __name__=='__main__':
    main()