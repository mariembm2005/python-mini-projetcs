from time import sleep
import random

class HumanPlayer:
    def __init__(self,s):
        self.s = s
class Board:
    def __init__(self,liss):
        self.liss = liss
class Game:
    def __init__(self,brd,p1,p2):

        self.brd = brd
        self.liss = brd.liss
        self.lis = "\n".join(self.liss[i] * 3 for i in range(3))
        self.p1 = p1
        self.p2 = p2
        self.update_lis()
    def update_lis(self):
        self.lis = "\n".join(" ".join(self.liss[3 * i + j] for j in range(3)) for i in range(3))
    def user1(self):
        n = int(input("input number between 1 and 9 :"))
        while n < 1 or n > 9:
            print("Choose the right choice!!!")
            sleep(1)
            n = int(input("input number between 1 and 9 :"))
        while True:
            if self.liss[n - 1] != "  -  ":
                print("Choose another number,bc that is taken")
                n = int(input("input number between 1 and 9 :"))
            else:
                break
        self.liss[n - 1] = f"  {self.p1.s}  "
        self.update_lis()

    def comp(self):
        n = random.randint(1, 9)
        while self.liss[n - 1] != "  -  ":
            n = random.randint(1, 9)
        self.liss[n - 1] = f"  {self.p2.s}  "
        self.update_lis()
    def verify(self,s):
        ok = False
        for i in range(0, 9, 3):
            ok = self.liss[i] == self.liss[i + 1] == self.liss[i + 2] == s
            if ok:
                return ok
        for i in range(0, 3):
            ok = self.liss[i] == self.liss[i + 3] == self.liss[i + 6] == s
            if ok:
                return ok
        ok = self.liss[0] == self.liss[4] == self.liss[8] == s
        if ok:
            return ok
        ok = self.liss[2] == self.liss[4] == self.liss[6] == s
        return ok

    def completee(self):
        for x in self.liss:
            if x == "  -  ":
                return False
        return True

    def play(self):
            print("First state".center(20, "*"))
            print(self.lis)
            while True:
                print("*********************")
                self.user1()
                print(self.lis)
                if self.verify(f"  {self.p1.s}  "):
                    print("You win :)")
                    break
                if self.completee():
                    print("Tie")
                    break
                sleep(1)
                print("*********************")
                self.comp()
                print("*********************")
                print(self.lis)
                if self.verify(f"  {self.p2.s}  "):
                    print("computer wins :(")
                    break
                if self.completee():
                    print("Tie")
                    break
                sleep(1)


player1 = HumanPlayer("X")
player2 = HumanPlayer("O")
liss = ["  -  " for j in range(9)]
my_board = Board(liss)
my_game = Game(my_board,player1,player2)
my_game.play()