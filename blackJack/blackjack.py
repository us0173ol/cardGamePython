
from dealer import *
from player import *
from deck import *
from card import *
#this is basically from https://github.com/minneapolis-edu/pig_py_tests/blob/master/pig
def number_of_players(question, min=1):
#this is called from game.py, essentially its useless for now since this program is
#designed for only one player and one dealer, but this makes sure the number is positive
#and not 0
    valid = None
    while not valid:
        valid = int(input(question + ': '))
        if valid < min:
            valid = None
            print("Choose a number higher than 0")
            break
        return valid
#getNames will loop through the number of players and get their names 
def getNames(number, type_of_object):

    names = []
    for n in range(number):
        name = input("What is the name of {} {}: ".format(type_of_object, n + 1))

        while name in names:
            name = input('There is already a {} with that name.  Please enter the name of {} {}'.format(type_of_object, type_of_object, n + 1))

        names.append(name)
    return names
