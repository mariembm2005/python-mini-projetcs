import random
import time

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]
class hangman:
    def __init__(self,word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_'*len(self.word_to_guess))
    def find_indexes(self,letter):
        return [i for i,c in enumerate(self.game_progress) if letter==c]
    def is_invalid_letter(self,input_):
        return len(input_)!=1 or not input_.isalpha()
    def play(self):
        is_running = True
        while is_running:
            guess = input("Enter a letter: ").upper()
            if self.is_invalid_letter(guess):
                print('Invalid input')
                time.sleep(1)
                continue
            if self.find_indexes(guess)!=[]:
                print(f"{guess} is already guessed")
                time.sleep(1)
                continue
            if guess in self.word_to_guess:
                for i in range(len(self.word_to_guess)):
                    if self.word_to_guess[i]==guess:
                        self.game_progress[i] = guess
                print(self.game_progress)
            else:
                self.failed_attempts+=1
                for i in range(1,self.failed_attempts+1):
                    print(HANGMAN[i])
                print(self.game_progress)

            if "_" not in self.game_progress:
                print(self.word_to_guess)
                print("YOU WIN")
                is_running = False
            elif self.failed_attempts>=len(HANGMAN)-1:
                print(self.word_to_guess)
                print("YOU LOSE")
                is_running = False





def main():
    word = random.choice(WORDS)
    print(word)
    hung = hangman(word)
    hung.play()
if __name__=='__main__':
    main()


