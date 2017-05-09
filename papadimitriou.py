import random
import os
import fileinput
import math
import pycosat

clauses = []
vars = []

def main():
    text = open("test.txt")
    line = text.readline()
    line = line.split(" ")
    numVars = int(line[0])
    print("Number of variables: ", numVars)
    for i in range(numVars-1):
        newline = text.readline().rstrip()
        newline = newline.split(" ")
        print(newline)
        clauses.append((int(newline[0]), int(newline[1])))
    for i in range(numVars):
        vars.append(random.randint(0, 1))
    falseClauses = returnFalseClases(clauses)
    k = 2*numVars*numVars
    while len(falseClauses) > 0 and k > 0:
        k = k - 1
        #print(falseClauses)
        flipper = random.choice(falseClauses)
        #print(flipper)
        access = abs(random.choice(flipper))
        if vars[access] == 0:
            vars[access] = 1
        else:
            vars[access] = 0
        falseClauses = returnFalseClases(clauses)
    if len(falseClauses) == 0:
        print("Satisfiable for the variables: ", vars)
        return
    else:
        print("Not Satisfiable")
        return

def returnFalseClases(clauselist):
    trueClauses = []
    falseClauses = []
    for clause in clauselist:
        firstNegated = False
        secondNegated = False
        if clause[0] < 0:
            firstNegated = not firstNegated
        if clause[1] < 0:
            secondNegated = not firstNegated
        firstC = clause[0]
        first = vars[abs(firstC)-1]
        secondC = clause[1]
        second = vars[abs(secondC)-1]
        if not firstNegated and not secondNegated:
            trueClauses.append((firstC, secondC)) if first or second else falseClauses.append((firstC, secondC))
        elif firstNegated and not secondNegated:
            trueClauses.append((firstC, secondC)) if not first or second else falseClauses.append((firstC, secondC))
        elif not firstNegated and secondNegated:
            trueClauses.append((firstC, secondC)) if first or not second else  falseClauses.append((firstC, secondC))
        else:
            trueClauses.append((firstC, secondC)) if not first or not second else falseClauses.append((firstC, secondC))
    return falseClauses;

main()