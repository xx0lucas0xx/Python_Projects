#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To utalize the concept of abstraction
#
# Tested OS:  This code was written and tested to work with Windows 11.


from abc import ABC, abstractmethod
class prize(ABC):
    def ticketsWon(self, amount):
        print("your ticket count: ",amount)
    # passing in an unknown argument
    @abstractmethod
    def goal(self, amount):
        pass

class exchange(prize):
    # defined how to implement the goal function from its parent ticketsWon class
    def goal(self, amount):
        print("you need {} tickets, so you sadly don't have enough to get the sonic plush yet :(".format(amount))

obj = exchange()
obj.ticketsWon(136)
obj.goal(777)


    
