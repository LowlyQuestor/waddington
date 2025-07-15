# TODO: add code to simulate environment for the creatures
import creature as c
import random as rand

class Environment:
    population_cap = 5
    creatures = []
    
    def __init__(self):
        self.temp = rand.randint(1, 100)
        self.totalCreaturesEver = 0

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
        pop = len(self.creatures)
        acc = 0
        openSpots = self.population_cap - pop
        if pop < self.population_cap:
            print("new spots avaliable:", openSpots)
        while acc < openSpots:
            parentOrganism = rand.choice(self.creatures)
            self.reproduceCreature(parentOrganism)
            print(parentOrganism.getId(), "begot", self.creatures[-1].getId())
            acc += 1

    def reproduceCreature(self, parent):
        newId = len(self.creatures) + 1 # id of new creature is one after last creature
        temp = c.Creature(newId)
        temp.setOffspringGenomeAce(parent)
        self.creatures.append(temp)
            

    def print(self):
        print("\nEnvironment summary")
        print("Temperature: ", self.temp, "\n")
        print("Current Population: \n")

        for i in self.creatures:
            i.printCreature()
            print("\n")

    def setRandTemp(self):
        self.temp = rand.randint(1,100)

p = Environment()
p.populate(5)
acc = 1
continue_answer = "y"
while continue_answer == "y":
    print("\n \n \ngeneration:" + str(acc))
    acc += 1
    p.print()
    p.setRandTemp()
    p.cullPopulation()
    p.reproduction()
    continue_answer = input("Continue? y/n ")
