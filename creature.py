# TODO: create a prototype for the simulated creature
import random
class Genome:
    threshold = 0
    def __init__(self):
        self.genes = []
         
    
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

    def mutate(self):
        if len(genes) != 0:
            chance = random.randint(0, 100)
            if chance > 25:
                i = random.randint(0,4)
                self.genes[i] = not(self.genes[i])
                self.calcThresh()
                
    def getThresh(self):
          return self.threshold

    def print(self):
        print("Gene summary\n", self.genes, "\n", self.threshold)
        
    

 
class Creature:
    def __init__(self, idnum):
        self.idNum = idnum
        self.genome = Genome()

    def setRandomGenome(self):
        self.genome.makeRandomGenome()

    def mutate(self):
        self.genome.mutate()
        
    def getId(self):
        return self.idNum

    def getThresh(self):
        return self.genome.getThresh()
    
    def print(self):
        print("Creature id: ", self.idNum, "\n",
              "Creature threshold: ", self.getThresh())
        print(self.genome.genes)
#        self.genome.print()
