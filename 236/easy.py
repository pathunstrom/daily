#!python

import random


pieces = ["O", "I", "S", "Z", "L", "J", "T"]

def bag(lot):
    bag = lot[:]
    random.shuffle(bag)
    while bag:
        yield bag.pop()

def finite_bag(number, lot):
    _bag = bag(lot)
    for _ in xrange(number):
        try:
            yield next(_bag)
        except StopIteration:
            _bag = bag(lot)
            yield next(_bag)

if __name__ == "__main__":
    print("".join(finite_bag(50, pieces)))
