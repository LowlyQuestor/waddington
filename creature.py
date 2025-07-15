# TODO: create a prototype for the simulated creature
import random

class Genome:
    threshold = 0
    def __init__(self):
        self.genes = []
        self.idnum = "0"
    
    def calcThresh(self):
         acc = 0
         for i in self.genes:
              if i == 1:
                   acc += 1
              else:
                   continue
              self.threshold = (100 - (20 * acc))


    def makeRandomGenome(self):
        i = 0
        while i < 5:
             self.genes.append(random.randint(0,1))
             i += 1
        self.calcThresh()

    def mutate(self):
        s = random.randint(0,4)
#        print("[DEBUG] gene selected", s)
        if self.genes[s] == 0:
            self.genes[s] = 1
        else:
            self.genes[s] = 0
        self.calcThresh()
        self.genes[0] = "M"

                
    def getThresh(self):
          return self.threshold

    
    def getGenesString(self):
        geneString = "".join(map(str, self.genes))
        geneString = geneString.replace("True", "X")
        geneString = geneString.replace("False", "O")
        return geneString

    def getGenes(self):
        return self.genes

    def print(self):
        print("Gene summary\n", self.genes, "\n", self.threshold)
        
    

 
class Creature:
    def __init__(self, idnum):
        self.idnum = idnum
        self.genome = Genome()
        self.parentId = "?"

    def setRandomGenome(self):
        self.genome.makeRandomGenome()

    def setOffspringGenomeAce(self, parent):
        self.parentId = parent.getId()
        self.genome.genes = parent.getGenes().copy()
#        print("[DEBUG] Genome size:", len(self.genome.genes))
        self.genome.mutate()
        
    def getId(self):
        return self.idnum

    def getThresh(self):
        return self.genome.getThresh()
    
    def getGenesString(self):
        return self.genome.getGenesString()
    
    def getGenes(self):
        return self.genome.getGenes()
    
    def getParent(self):
        return self.parentId
    
    def printCreature(self):
        print("Creature id: ", self.idnum, "\n",
              "Creature threshold: ", self.getThresh(), "\n",
              "Creature Parent:", self.getParent())
        print(self.getGenesString())
