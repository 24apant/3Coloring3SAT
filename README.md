# 3Coloring3SAT
Proving 3 Coloring is NP-Complete by reducing 3SAT to 3 Coloring



Download all files

config.py - Configuration file containing different global variables
objects.py - Objects for the Gadget and Node class, used in viz.py
viz.py - Main script and display loop, parses clauses and applies 3 coloring to 3 sat problem

input.txt - txt file of the 3 sat problem itself
 

sample input (sensitive):
 

A,B,C

!D,E,F



truths.txt - dictionary txt file of each literal in input.txt and its truth value ('True' or 'False')
 

sample input(sensitive) -

 
A,True

B,True

C,False

D,False

E,False

F,False

