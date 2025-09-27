import random
options = ("rock","paper","scissors")

playing = True
while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("enter a choice(rock,paper,scissors) : ")
    print(f"player : {player}")
    print(f"computer : {computer}")
    if player==computer:
        print("It's a Tie!")
    elif player=="rock" and computer=="scissors":
        print("you win!")
    elif player=="paper" and computer=="rock":
        print("ou win!")
    elif player=="scissors" and computer=="paper":
        print("You win!")
    else:
        print("You lose!")
    if not input("play again? (y/n) : ").lower()=="y":
        playing = False
print("Thanks for playing! ")
