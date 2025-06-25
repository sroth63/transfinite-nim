from ordinals import *

class Nim:
    def __init__(self, rows):
        self.rows = rows
    
    def __repr__(self):
        repr = ""
        for row in self.rows:
            repr += "\n" + row.__repr__()
        return repr[1:]
    
    def replace(self, index, alpha):
        assert self.rows[index] > alpha
        if alpha == 0:
            self.rows.pop(index)
        else:
            self.rows[index] = alpha
    
    def grundy(self):
        gr = 0
        for row in self.rows:
            gr ^= row
        return gr

    def play(self):
        turn = 0 # 0 = computer, 1 = player
        print("Current position:")
        print(self)
        while self.rows != []:
            if turn == 0:
                if self.grundy() == 0: # No guaranteed winning strategy
                    index = 0
                    alpha = 0 
                else:
                    for i in range(len(self.rows)):
                        a = self.rows[i] ^ self.grundy()
                        if a < self.rows[i]:
                            index = i
                            alpha = a
                            break
                self.replace(index, alpha)
                print("------------------")
                print("I choose row", index)
                print("Current position:")
                print(self)
                turn = 1-turn
            else:
                print("------------------")
                print("Select the index of a row (between 0 and " + str(len(self.rows)-1) + ")")
                index = int(input())
                print("Select how many objects you want on this row (between 0 and " + str(self.rows[index]) + " excluded)")
                alpha = eval(input())
                self.replace(index, alpha)
                print("Current position:")
                print(self)
                turn = 1-turn
        print("Game finished")
        if turn == 0: print("You won!")
        else: print("I won!")
        

print("~~~Transfinite Nim Game~~~")
print("Enter an initial configuration for Nim")
print("Example : [2, 1, omega, omega*7+42, omega**omega * 4 + 1729]")
Nim(eval(input())).play()
