import re
import sys
import math


class gramaticaIC:
    initial = None;
    nonTerminals = None;
    terminals =  None;
    productions = None;
    ok = 0;
    length = 0;


    def __init__(self, initial, nonTerminals,terminals,productions):
        self.initial = initial
        self.nonTerminals = nonTerminals
        self.terminals = terminals
        self.productions = productions

    def __str__(self):
        return "Initial: {0}\nNonTerminal: {1}\nTerminals: {2}\nProductions:\n{3}".format(self.initial," ".join(self.nonTerminals)," ".join(self.terminals),"\n".join(str(x)+ ' ->  ' + " ".join(y)for x,y in self.productions.items()))

    def generateAll(self,myString):
        nonTermCount = re.findall("<[A-Z]",myString)
        originalSize = len(myString) - len(nonTermCount)*2
        if originalSize > self.length:
            return -1
        if nonTermCount[0] not in self.productions.keys():
            return -1
        if len(nonTermCount) > self.length:
            return -1
        for x in self.productions[nonTermCount[0]]:
            pos = myString.find(nonTermCount[0])
            adder = x
            if(adder == 'ε' or adder == 'λ'):
                adder = ''
            newString = myString[:pos] + adder + myString[pos+2:]
            newNonTermCount = re.findall("<[A-Z]",newString)
            #if len(adder)>=4 and adder[0:2] == nonTermCount[0] and 
            if(len(newNonTermCount)==0 and len(newString)<=self.length):
                print(newString)
                self.ok=1
            else:
                self.generateAll(newString)
    
    def getAllWords(self,length):
        self.ok=0
        self.length = length
        self.generateAll("<"+self.initial)
        if self.ok == 0:
            print("No words found")
        self.ok=0


def main():
    gramatica = None
    myfile = "gramatics.in"

    if(len(sys.argv)>=2):
        myfile = sys.argv[1]

    with open(myfile,'r') as cin:
        ok = cin.readline().strip()
        if(ok.upper() != "BEGINTEST"):
            print("Wrong input")
            exit()
        prod = dict()
        nonTerm = cin.readline().split()
        term = cin.readline().split()
        init = cin.readline().strip()
        inp = cin.readline().strip()
        while(inp.upper() != "ENDTEST"):
            inp = re.split(' > ',inp,1)
            prod["<"+inp[0]] = re.split(' \| ',inp[1])
            inp = cin.readline().strip()

        for key,data in list(prod.items()):
            for x in data:
                finder = re.findall("<[A-Z]",x)
                if len(finder)*2 == len(x):
                    if finder[0] not in prod.keys():
                        continue
                    for y in list(prod[finder[0]]):
                        new = y + x[2:]
                        if x!=y and (new not in prod[finder[0]]) and y!="ε" and y!="λ":
                            prod[finder[0]].append(new)
                    prod[key].remove(x)
                            
        gramatica = gramaticaIC(init,nonTerm,term,prod)

    print(gramatica)
    print("Enter number of tests:")
    n = int(input("n="))
    for i in range(1,n+1):
        print("Enter test number " + str(i) +":")
        tester = int(input(str(i)+"="))
        gramatica.getAllWords(tester)
            

if __name__ == "__main__":
    main()

