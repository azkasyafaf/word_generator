from itertools import permutations
import enchant
import os

running = True

class Application():
    def __init__(self):
        self.inp = []
        self.d = enchant.Dict("en_US")
        self.op = set()
    
    def generator(self, inp, minLength = 2):
        self.op.clear()

        for n in range(len(inp)):
            for word in list(permutations(inp,n+1)):
                temp_out = "".join(word)
                if len(temp_out) > minLength:
                    if self.d.check(temp_out):
                        self.op.add(temp_out)
        
        print(sorted(self.op, key=len, reverse=False))
        print("\nWords found: {}".format(len(self.op)))

def start(app):
    temp_inp = input("Input your words: ")
    min_length = input("What is the minimum lenght? ")

    app.inp = [x.lower() for x in temp_inp]
    min_length = 2 if (min_length == "") else int(min_length)

    print("\n--------------\n")
    app.generator(app.inp, min_length)
    print("\n--------------\n")

def main():
    global running

    while running:
        start(Application())

        while True:
            temp_inp = input("\nDo you want to try again? (Y/N) ")
            print("\nPlease wait...\n")
            
            if temp_inp.upper() == "N":
                running = False
                break
            elif temp_inp.upper() == "Y":
                os.system("clear")
                break
            else:
                print("Error. Command not found")
    print("Exiting...\n\n")
    
main()