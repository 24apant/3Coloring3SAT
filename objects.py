import pygame
import config


# Gadget object used in displaying
class Gadget:
    def __init__(self, gui=None, frame=[0, 0, config.GUI_W, config.GUI_H]):

        # fancy thing where we can resize the entire gadget
        self.w = frame[2] - frame[0]
        self.h = frame[3] - frame[1] 
        self.TL = frame[0:2]

        self.gui = gui # reference to the gui

        # columns (x and y) where the gadgets align
        gCol1 = self.TL[0] + (self.w//2) - (3 * config.NODE_RADIUS)
        gCol2 = self.TL[0] + (self.w//2) 
        gCol3 = self.TL[0] + (self.w//2) + (3 * config.NODE_RADIUS)


        # Gadget().nodes is a 2d array of nodes - each row is a row in the gadget and each element is a node in the gadget in respective row        
        self.nodes =[
                    [Node([gCol2, 2*config.NODE_RADIUS])],
                    [Node([gCol1, 5*config.NODE_RADIUS]), Node([gCol2, 5*config.NODE_RADIUS]), Node([gCol3, 5*config.NODE_RADIUS])], # clauses
                    [Node([gCol1, 8*config.NODE_RADIUS]), Node([gCol2, 8*config.NODE_RADIUS]), Node([gCol3, 8*config.NODE_RADIUS])], # first gadget
                    [Node([gCol1 - (3 * config.NODE_RADIUS), 11*config.NODE_RADIUS]),Node([gCol1, 11*config.NODE_RADIUS]), Node([gCol2, 11*config.NODE_RADIUS]), Node([gCol3, 11*config.NODE_RADIUS]), Node([gCol3+(3*config.NODE_RADIUS), 11*config.NODE_RADIUS])],#last gadget and t and false
                    ]
        

        # set up connections between nodes - important for checking neighbors'colors
        
        # Buffer to top 3 
        self.attach(self.nodes[0][0], self.nodes[1][0])
        self.attach(self.nodes[0][0], self.nodes[1][1])
        self.attach(self.nodes[0][0], self.nodes[1][2])

        # True Node to Middle 3
        self.attach(self.nodes[-1][0], self.nodes[2][0])
        self.attach(self.nodes[-1][0], self.nodes[2][1])
        self.attach(self.nodes[-1][0], self.nodes[2][2])

        # 1st row to 2nd row
        self.attach(self.nodes[1][0], self.nodes[2][0])
        self.attach(self.nodes[1][1], self.nodes[2][1])
        self.attach(self.nodes[1][2], self.nodes[2][2])

        # 2nd row to 3rd row
        self.attach(self.nodes[2][0], self.nodes[3][1])
        self.attach(self.nodes[2][1], self.nodes[3][2])
        self.attach(self.nodes[2][2], self.nodes[3][3])

        # T to left gadget corner and F to right gagdet corner
        self.attach(self.nodes[-1][0], self.nodes[-1][1])
        self.attach(self.nodes[-1][-1], self.nodes[-1][-2])

        # Bottom row
        self.attach(self.nodes[-1][1], self.nodes[-1][2])
        self.attach(self.nodes[-1][2], self.nodes[-1][3])


        # set buffer, true, and false in gadget
        self.nodes[0][0].set("Buffer")
        self.nodes[-1][0].set("True")
        self.nodes[-1][-1].set("False")
    
    def attach(self, n1, n2):
        # attaches two nodes together by appending their neighbors to each other
        n1.neighbors.append(n2)
        n2.neighbors.append(n1)
        
    def draw(self):
        # draw all attachments first
        for row in self.nodes:
            for node in row:
                node.drawAttachments(self.gui)

        for row in self.nodes:
            for node in row:
                node.draw(self.gui)

# Individual node class in gadget - keeps track of its value and neighbors
class Node:
    def __init__(self, coords):

        self.value = "" # means blank/empty
        self.x = coords[0]
        self.y = coords[1]
        self.color = (255, 255, 255)
        self.neighbors = [] # empty for now, parent Gadget will attach nodes together.
    
    def drawAttachments(self, gui):
        # Draws all lines that attach this node to its neighbors
        for n in self.neighbors:
            pygame.draw.line(gui, (0, 0, 0), [self.x, self.y], [n.x, n.y])

    def draw(self, gui):
        # draws a circle representing itself and its color
        pygame.draw.circle(gui, self.color, [self.x, self.y], config.NODE_RADIUS)
        pygame.draw.circle(gui, (0,0,0), [self.x, self.y], config.NODE_RADIUS, 2)
        
    def set(self, val):
        # sets a value - parameter checking to make sure the input is valid
        if val == "True":
            self.color=config.GREEN
        elif val == "False":
            self.color=config.RED
        elif val == "Buffer":
            self.color = config.BLUE
        else:
            raise BaseException("Value '" + val + "' not valid.")
        self.value = val
    

