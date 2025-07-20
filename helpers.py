# Here lies helper functions for the rest of the codebase
import random as r


def doNtimes(func, n, args=None):  # Run function n times iteratively for speed
    acc = 0
    if args is not None:
        while acc < n:
            func(args)
            acc += 1
    else:
        while acc < n:
            func()
            acc += 1


def randomlyDo(func, chance, args=None):  # Do func at random based on chance
    lh = r.randint(1, chance)
    if args is not None:
        if lh < chance:
            func(args)
        else:
            return None
    else:
        if lh < chance:
            func()
        else:
            return None
