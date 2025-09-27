import random
class Solution:
    def getHint(self, secret, guess):
        a = 0
        lis = list(secret)
        lis2 = list(guess)
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                a += 1
                lis2[i] = "*"
                lis[i] = "*"
        b = 0
        for i in range(len(guess)):
            if secret[i] != guess[i] and secret[i] in lis2:
                b += 1
                lis2[lis2.index(secret[i])] = "*"
                lis[i] = "*"

        return str(a) + "A" + str(b) + "B"

def nodups(n):
    num = [int(i) for i in str(n)]
    if len(num)==len(set(num)):
        return True
    else:
        return False
def generateNum():
    while True:
        num = random.randint(1000,9999)
        if nodups(num):
            return num
if __name__=='__main__':
    num = generateNum()
    tries = int(input("Enter number of tries: "))
    while tries>0:
        guess = int(input("Enter your guess: "))
        if not nodups(guess):
            print("Number should not have repeated digits. Try again.")
            continue
        if guess<1000 or guess>9000:
            print("Enter 4 digit number only. Try again.")
            continue
        sol = Solution()
        bull_cow = sol.getHint(str(num),str(guess))
        print(bull_cow)
        tries-=1
        if bull_cow[0]==4:
            print("Right congrats!!!!")
            break
    print(f"You ran out of tries.Number was {num}")
