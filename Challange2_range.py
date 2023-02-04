#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To test out the range function
#
# Tested OS:  This code was written and tested to work with Windows 11.

num_list = ['1', '2', '3', '4', '5', '6']
num_list_len = len(num_list)
for i in range(0, num_list_len):
    print(num_list[i])


range(10)[::-1]
 # range(9, -1, -1)
