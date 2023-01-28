#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To make use of different types of encapsulations
#
# Tested OS:  This code was written and tested to work with Windows 11.


# establishing a class called fruit
class fruit:
    def __init__(self):
        self._protectedVar = '' # adding a protected variable that's empty

obj = fruit()
obj._protectedVar = 'Oranges' # passing in the string to the protected var
print("I love " + obj._protectedVar + " they are very tasty")


# establishing a class called veggie

class veggie:
    def __init__(self):
        self.__privateVar = 'Carrots' # adding a private variable

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = veggie()
obj.getPrivate() 
obj.setPrivate('Cucumbers') # changing the private variable
obj.getPrivate()



