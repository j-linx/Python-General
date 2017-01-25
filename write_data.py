# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:29:49 2016

@author: Michael Waters
"""

from math import sin

x = []
y = []
for i in range(40):
    x.append( i*0.1)
    y.append(sin( i*0.1))
    
    
myfile = open('data.txt', 'w')    
for i in range(40):
        myfile.write('%f\t%f\n'%(x[i],y[i]))
        
myfile.close()

#myfile is a file identifier (or object)
#.write is function of that
#it writes the string you give to it to the file
#it appends them to file.
#'%f meters to home' % distance_to_home
#converts the floating point number stored in distance_to_home to a string like 23.78 and inserts it in the string
#\t creates a tab character
#\n creates a new line