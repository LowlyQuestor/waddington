# TODO: add code to simulate environment for the creatures
import creature as c
import random as rand

class Environment:
    temp = 0
    population_cap = 5
    totalCreaturesEver = 0
    creatures = []
    def __init__(self):
        self.temp = rand.randint(1, 100)


    def populate(self, n): # populate environment with n # of creatures
        acc = 0
        while acc < n:
            self.creatures.append(c.Creature(acc))
            self.creatures[acc].setRandomGenome()
            acc += 1
            self.totalCreaturesEver += 1

    def cullPopulation(self): # checks to see if creatures in enviornment survive
        chance = rand.randint(1, 100)
        acc = 0
        for i in self.creatures:
            myId = self.creatures[acc].getId()
            if self.creatures[acc].getThresh() < self.temp:
                if chance < 50:
                   print("creature " + str(myId) + " has perished")
                   self.creatures.remove(i)
            acc += 1

    def reproduction(self):
        pop = 0
        acc = 0
        for i in self.creatures:
            pop += 1
        openSpots = self.population_cap - pop
        if pop < self.population_cap:
            print("reproduce this many times:", openSpots)
        while acc < openSpots:
            parentOrganism = rand.choice(self.creatures)
            parentGenes = parentOrganism.getGenes()
            parentId = parentOrganism.getId()
            self.creatures.append(c.Creature(self.totalCreaturesEver))
            self.creatures[-1].setOffspringGenomeAce(parentGenes, parentId)
            self.totalCreaturesEver += 1
            acc += 1



    def print(self):
        print("\nEnvironment summary")
        print("Temperature: ", self.temp, "\n")
        print("Current Population: \n")

        for i in self.creatures:
            i.printCreature()
            print("\n")

p = Environment()
p.populate(5)
acc = 1
continue_answer = "y"
while continue_answer == "y":
    print("\n \n \ngeneration:" + str(acc))
    acc += 1
    p.print()
    p.__init__()
    p.cullPopulation()
    p.reproduction()
    continue_answer = input("Continue? y/n")