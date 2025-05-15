# TODO: create a prototype for the simulated creature
import random

def getThresh(loci):
    acc = 0
    for i in loci:
        if i == True:
            acc = acc + 1
        else:
            continue
    return ((100 - (acc * 20)))

    
def makeGenome(loci):
     return {
         "genetics" : loci,
         "thresh" : getThresh(loci)
         }

class Creature:
    def __init__(self, idnum, genome):
        self.idNum = idnum
        self.genome = genome
    
