# you can try this by running python testing_tool.py python3 number_guessing.py
class Guesser:
    def __init__(self, a, b, n):
        self.start = a + 1
        self.end = b

    def guess(self):
        return self.start + (self.end - self.start)//2

    def set_ceil(self, ceil):
        self.end = ceil - 1

    def set_floor(self, floor):
        self.start = floor + 1


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        a, b = map(int, input().split(" "))
        n = int(input())
        guesser = Guesser(a, b, n)
        guessed = False
        while not guessed:
            guess = guesser.guess()
            print(guess)
            ans = input()
            if ans == 'TOO_SMALL':
                guesser.set_floor(guess)
            elif ans == 'TOO_BIG':
                guesser.set_ceil(guess)
            elif ans == 'CORRECT':
                guessed = True
            elif ans == 'WRONG_ANSWER':
                return


read_input()
