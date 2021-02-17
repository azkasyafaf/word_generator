from itertools import permutations
import enchant
import os

class Application():
    def __init__(self):
        self.inp = []
        self.d = enchant.Dict("en_US")
        self.op = set()
    
    def generator(self, inp, minLength = 2):
        temp_out = ""
        for n in range(len(inp)):
            for word in list(permutations(inp,n+1)):
                temp_out = "".join(word)
                if len(temp_out) > minLength:
                    if self.d.check(temp_out):
                        self.op.add(temp_out)
        print(sorted(self.op, key=len))
        print("\nWords found: {}".format(len(self.op)))

def main():
    while True:
        app = Application()
        temp_inp = input("Input your words: ")
        min_length = input("What is the minimum lenght? ")

        app.inp = [x.lower() for x in temp_inp]
        min_length = 2 if (min_length == "") else int(min_length)

        print("\n--------------\n")
        app.generator(app.inp, min_length)
        
        while True:
            temp_inp = input("\n--------------\n\nDo you want to try again? (Y/N) ")
            if temp_inp.upper() == "N" or temp_inp.upper() == "Y":
                print("\nPlease wait...\n")
                break
        
        if temp_inp.upper() == "N":
            print("Exiting...\n\n")
            break
        
        os.system("clear")
        app.op.clear()

main()
