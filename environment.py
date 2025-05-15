# TODO: add code to simulate environment for the creatures
import creature as c
import random as rand
class Environment:
    temp = 0
    creatures = []
    def __init__(self):
        self.temp = rand.randint(1, 100)


    def populate(self, n): # populate environment with n # of creatures
        acc = 0
        while acc < n:
            self.creatures.append(c.Creature(acc))
            self.creatures[acc].setRandomGenome()
            acc += 1


    def cullPopulation(self): # checks to see if creatures in enviornment survive
        chance = rand.randint(1, 100)
        acc = 0
        for i in self.creatures:
            if self.creatures[acc].getThresh() < self.temp:
                if chance < 50:
                   self.creatures.remove(i)
            acc += 1

    def print(self):
        print("Environment summary")
        print("Temperature: ", self.temp)

        for i in self.creatures:
            i.print()
        
