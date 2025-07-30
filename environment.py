# The environment and graveyard simulate darwinian selection
import creature as c
import random as rand
import helpers
import time


class Graveyard:
    creatures = dict()

    def __init__(self):
        return

    def add(self, c):
        self.creatures.update({c.getId(): c})


class Environment:
    creatures = dict()  # Allows using creature IDs as indexes
    graveYard = Graveyard()

    def __init__(self, cap):  # TODO: add debug mode
        self.temp = rand.randint(1, 100)
        self.populationCap = cap

    def __newId(self):  # Return the current nanosecond for unique id
        return time.time_ns()

    def __testCreature(self, creatureId):  # Randomly kill c if they cant survive
        if self.__isFit(creatureId):
            chance = rand.randint(1, 100)
            if chance >= 50:
                self.killCreature(creatureId)
                print("{} has perished".format(creatureId))
            else:
                print("{} survived, despite the odds".format(creatureId))

    def __isFit(self, creatureId):
        if self.getCreature(creatureId).getThresh() < self.temp:
            return False
        else:
            return True

    def addCreature(self):  # Adds random creature
        id = self.__newId()
        creature = c.Creature(id)
        creature.setRandomGenome()
        self.creatures.update({id: creature})  # Add creature to dict badly

    def populate(self, n):  # Populate with n creatures
        helpers.doNtimes(self.addCreature, n)

    def setRandTemp(self):
        self.temp = rand.randint(1, 100)

    def reproduceCreature(self, parentId):
        newId = self.__newId()
        temp = c.Creature(newId)
        temp.setOffspringGenomeAce(self.creatures.get(parentId))
        self.creatures.update({newId: temp})  # Add new creature

    def reproduction(self):  # Simulate random gene selection
        acc = 0
        self.printOpenSpaces()
        while acc < self.getOpenSpaces():  # while there's room
            parentOrganism = rand.choice(self.getCreatureList())
            self.reproduceCreature(parentOrganism.getId())
            print("{} has reproduced!".format(parentOrganism.getId()))
            acc += 1

    def killCreature(self, creatureId):
        self.graveYard.add(self.creatures.get(creatureId))
        self.creatures.pop(creatureId)  # Remove creature

    def cullPopulation(self):
        for i in self.getIdList():
            self.__testCreature(i)

    def getCreature(self, creatureId):
        return self.creatures.get(creatureId)

    def getCreatureList(self):
        return list(self.creatures.values())  # Does not return list by default

    def getIdList(self):
        return list(self.creatures.keys())

    def getPopulation(self):
        return len(self.getCreatureList())

    def getPopulationCap(self):
        return self.populationCap

    def getOpenSpaces(self):
        return self.getPopulationCap() - self.getPopulation()

    def print(self):
        print("\nEnvironment Summary\nTemperature: {}".format(self.temp))
        print("Total population: {}".format(self.getPopulation()))

    def printOpenSpaces(self):
        if self.getPopulation() < self.getPopulationCap():  # if there's room
            print("{} new spots are avaliable".format(self.getOpenSpaces()))
        else:
            print("No new spaces avaliable in environment")
