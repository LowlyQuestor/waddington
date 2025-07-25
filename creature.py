import random
import helpers


class Genome:
    def __init__(self):
        self.threshold = 0
        self.genes = []
        self.idnum = 0
        self.size = 5

    def __countOnGenes(self):
        '''Counts the number of genes in Genome that are turned on (== 1)'''
        acc = 0
        for i in self.genes:
            if i == 1:
                acc += 1
            else:
                continue
        return acc

    def __changeGene(self, g):
        '''Changes single gene (g) to opposite of previous state (on/off)'''
        if g == 0:
            g = 1
        else:
            g == 0

    def __calcThresh(self):
        '''Sets threshold to the max temperature genome can survive'''
        self.threshold = (100 - (20 * self.__countOnGenes()))

    def makeRandomGenome(self):
        '''Populate genes with a random genome and figure out the threshold'''
        helpers.doNtimes(self.genes.append, self.size, random.randint(0, 1))
        self.__calcThresh()

    def mutate(self):
        '''Mutates a random gene in genome'''
        s = random.randint(0, self.size - 1)  # random index in genes
        g = self.genes[s]  # Random gene
        self.__changeGene(g)

    def toString(self):
        '''Returns a pretty string version of gene list'''
        gs = "".join(map(str, self.genes))
        gs = gs.replace("1", "X")
        gs = gs.replace("0", "O")
        return gs

    def print(self):
        print("Genome summary")
        print("Genes: {}".format(self.toString()))
        print("Temperature threshold: {}".format(self.getThresh()))

    def getThresh(self):
        return self.threshold

    def getGenes(self):
        return self.genes


class Creature:
    def __init__(self, idnum):
        self.idnum = idnum
        self.genome = Genome()
        self.parentId = None

    def setRandomGenome(self):
        '''Gives a random genome to creature'''
        self.genome.makeRandomGenome()

    def setOffspringGenomeAce(self, parent):
        '''Makes a creature a genetic descendant of another'''
        self.parentId = parent.getId()
        self.genome.genes = parent.getGenes().copy()
        self.genome.mutate()

    def getId(self):
        return self.idnum

    def getParentId(self):
        return self.parentId

    def getThresh(self):
        return self.genome.getThresh()

    def getGenes(self):
        return self.genome.genes

    def getGenesAsString(self):
        return self.genomes.toString()

    def print(self):
        print("Creature id: {}".format(self.idnum))
        print("Creature threshold: {}".format(self.getThresh()))
        print("Creature parent: {}".format(self.getParentId()))
        print("Creature genes: {}".format(self.getGenesAsString()))
