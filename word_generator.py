from itertools import permutations
import enchant
import os

class Application():
    def __init__(self):
        self.inp = []
        self.d = enchant.Dict("en_US")
        self.op = set()
    
    def generator(self, inp):
        temp_out = ""
        for n in range(len(inp)):
            for word in list(permutations(inp,n)):
                temp_out = "".join(word)
                if self.d.check(temp_out):
                    op.add(temp_out)
        print(self.op)

def main():
    app = Application()
    while True:
        temp_inp = input("Input your words: ")
        app.inp = [x.lower() for x in temp_inp]
        print("\n--------------\n")
        app.generator(app.inp)
        while True:
            temp_inp = input("\n--------------\n\nDo you want to try again? (Y/N) ")
            if temp_inp.upper() == "N" or temp_inp.upper() == "Y":
                print("\nPlease wait...\n")
                break
        if temp_inp.upper() == "N":
            print("Exiting...\n\n")
            break
        os.system("cls")

main()