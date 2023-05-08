# Visualizes 3SAT problem as a graph coloring algorithm
import os

def parse_file(filename):
    clauses = []
    if filename in os.listdir():
        text_input = open(filename).readlines()

        for idx in range(len(text_input)-1):
            text_input[idx] = text_input[idx][0:len(text_input[idx])-1]

        for stri in text_input:
            split = stri.split(",")
            clauses.append(split)
    else:
        print("Couldn't find file " + filename + ": check os.listdir()")
    return clauses

if ('input.txt' in (x:= os.listdir()) and 'truths.txt' in x):

    # Parse input.txt and add each clause to clauses
    clauses = parse_file('input.txt')    

    # Parse truth.txt and make a dictionary
    truths = {}
    truth_list = parse_file('truths.txt')
    for t in truth_list:
        if t[1] != "True" and t[1] != "False":
            raise BaseException("Truth argument " + str(t) + " has invalid declaration: must be 'True' or 'False'.")
        truths[t[0]] = bool(t[1])
    
    # Make sure clauses are valid and readable
    for c in clauses:
        for i in range(len(c)):
            c[i] = c[i].strip()
            s = c[i]
            if(len(s) > 2 or len(s) == 0):
                raise BaseException("Clause " + str(c) + " has invalid literal " + str(s))
            if(len(s) == 2 and s[0] != '!'):
                raise BaseException("Clause " + str(c) + " has invalid literal " + str(s))
            if (s[-1] in "1234567890@#!$%^&*()-=_+<>,./?;:'`~"):
                raise BaseException("Clause " + str(c) + " has invalid literal " + str(s))
