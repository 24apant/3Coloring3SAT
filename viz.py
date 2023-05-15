# Visualizes 3SAT problem as a graph coloring algorithm
import os
import pygame
import objects
import config
import sys
import keyboard

pygame.init()
screen = pygame.display.set_mode((config.GUI_W, config.GUI_H))
fps = pygame.time.Clock()
gadget = objects.Gadget(gui=screen)



def colorGadget(gadget):
    # colors and returns a value to color a gadget

    # go through each node that does not have a color and check their neighbors
    for row in gadget.nodes:
        for node in row:
            if node.value == "":
                # check if it has any limitations on its neighhbors

                # map of colors and if they can apply to this node
                colors = {"True":True,"Buffer":True ,"False":True}
                for n in node.neighbors:
                    if n.value in colors: colors[n.value] = False
                # find an available color
                for c in colors.items():
                    if c[1] == True:
                        # set my color to c[0]
                        node.set(c[0])


def parse_file(filename):
    # for any file in the specified directory, parse the file and read its clauses and returns them
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

if ('input.txt' in (x:= os.listdir()) and 'truths.txt' in x): # if we can find the files in the current directory:

    # Parse input.txt and add each clause to clauses
    clauses = parse_file('input.txt')    

    # Parse truth.txt and make a dictionary
    truths = {}
    truth_list = parse_file('truths.txt')
    for t in truth_list:
        if t[1] != "True" and t[1] != "False":
            raise BaseException("Truth argument " + str(t) + " has invalid declaration: must be 'True' or 'False'.")
        truths[t[0]] = t[1] == "True"
        truths["!"+t[0]] = not(t[1] == "True")

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
            
    # keeps track of the current clause we are visualizing.
    curr_clause = 0

    # display loop
    while True:
        # refresh the screen
        screen.fill((255, 255, 255))

        # check if the X button has been clicked and if it has, sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        # get the current clause and set the corresponding nodes on the gadget to true/false from the clause
        c = clauses[curr_clause]
        for idx, s in enumerate(c):
            #evaluate the s
            if truths[s] == True:
                gadget.nodes[1][idx].set("True")
            else:
                gadget.nodes[1][idx].set("False")


        
        gadget.draw()


        # applies graph coloring to the gadget on keypress 'f'
        if keyboard.is_pressed("f"):
            colorGadget(gadget)


        # updates the game
        pygame.display.update()
        pygame.display.set_caption(str(c)) # the caption of the screen is the clause being looked at.
        fps.tick(30)