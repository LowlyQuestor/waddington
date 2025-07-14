# TODO: create a prototype for the simulated creature
import random

class Genome:
    threshold = 0
    myParent = "?"
    def __init__(self):
        self.genes = []
        self.idnum = "0"
         
    
    def calcThresh(self):
         acc = 0
         for i in self.genes:
              if i == True:
                   acc += 1
              else:
                   continue
              self.threshold = (100 - (20 * acc))


    def makeRandomGenome(self):
        i = 0
        while i < 5:
             self.genes.append(bool(random.randint(0,1)))
             i += 1
        self.calcThresh()

    def setOffspringGenomeAce(self, parentGenes, parentId):
        chance = random.randint(0,100)
        self.genes = parentGenes
        geneSelected = random.randint(0,4)
        self.genes[0] = "M"
        self.myParent = str(parentId)
        self.calcThresh()
                
    def getThresh(self):
          return self.threshold

    def getParent(self):
          return self.myParent
    
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

    def setRandomGenome(self):
        self.genome.makeRandomGenome()

    def setOffspringGenomeAce(self, parentGenes, parentId):
        self.genome.setOffspringGenomeAce(parentGenes, parentId)
        
    def getId(self):
        return self.idnum

    def getThresh(self):
        return self.genome.getThresh()
    
    def getGenesString(self):
        return self.genome.getGenesString()
    
    def getGenes(self):
        return self.genome.getGenes()
    
    def getParent(self):
        return self.genome.getParent()
    
    def printCreature(self):
        print("Creature id: ", self.idnum, "\n",
              "Creature threshold: ", self.getThresh(), "\n",
              "Creature Parent:", self.getParent())
        print(self.getGenesString())