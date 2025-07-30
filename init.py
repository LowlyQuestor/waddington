#!/usr/bin/env python3
# TODO: Make program to start the simulation and allow for a basic command line
import environment as env

p = env.Environment(5)
p.populate(5)
choice = "y"
gen = 0
while choice == "y":
    print("\n generation: {}".format(gen))
    gen += 1
    p.setRandTemp()
    p.print()
    p.cullPopulation()
    p.reproduction()
    choice = input("Continue? y/n ")
