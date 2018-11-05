#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:33:18 2018

@author: heathercraddock
"""

import numpy as np, random as rnd
import math
import matplotlib.pyplot as plt
# testCases = rnd.sample(range(1, 100), 3)

def fitness(x):
    y = math.sin(math.pi*x/256)
    return y
def fitness2(x):
    y = ((2**(-2*((x-0.1)/0.9)**2)))*((math.sin(5*math.pi*x))**6)
    return y

def graph1():
    x=list(range(256))
    y = [fitness(xn) for xn in x]
    plt.plot(x,y)
    plt.show
def graph2():
    x=list(np.linspace(0, 1, 1000))
    y = [fitness2(xn) for xn in x]
    plt.plot(x,y)
    plt.show    
    
def eqn1():
    test_x = rnd.randint(0,256) # pick a random starting number
    # test_x = float("{0:.2f}".format(random.uniform(0, 1)))
    start_x = test_x
    temp_x = 0
    max_it = 100
    g = 1
    delta_x = 0.01
    t = 1
    incr_x = True
    step_size = delta_x
    f_test = fitness(start_x)
    stop = False
    max_x = 0
    no_improvement = False
    
    tempx1 = test_x + step_size
    tempx2 = test_x - step_size
    if fitness(tempx1)>=fitness(tempx2):
        incr_x = True
    else:
        incr_x = False
    
    while t < max_it and f_test != g and not no_improvement:
        if incr_x:
            temp_x = test_x + step_size
        else:
            temp_x = test_x - step_size
            
        if fitness(temp_x) >= fitness(test_x):
            if fitness(max_x) < fitness(temp_x):
                max_x = temp_x
            test_x = temp_x
            f_test = fitness(test_x)
            step_size = step_size + delta_x
            stop = False
        else:
            print("Reset")
            step_size = delta_x
            if stop:
                no_improvement = True
            stop = True
        print("Step: ",t,", Test: ",test_x, "Temp: ", temp_x)
        t += 1
     
    print("Start at ", start_x)    
    print("Iterations: ", t)
    print("Best x value: ", max_x)
    print("Best y value: ", fitness(max_x))
    
    return max_x


def eqn2():
    graph2()
    test_x = float("{0:.2f}".format(rnd.uniform(0, 1)))
    start_x = test_x
    temp_x = 0
    max_it = 100
    g = 1
    delta_x = 0.001
    t = 1
    incr_x = True
    f_test = fitness2(start_x)
    stop = False
    max_x = 0
    no_improvement = False
    
    tempx1 = test_x + delta_x
    tempx2 = test_x - delta_x
    if fitness2(tempx1)>=fitness2(tempx2):
        incr_x = True
    else:
        incr_x = False
    
    while t < max_it and f_test != g and not no_improvement:
        if incr_x:
            temp_x = test_x + delta_x
        else:
            temp_x = test_x - delta_x
            
        if fitness2(temp_x) >= fitness2(test_x):
            if fitness2(max_x) < fitness2(temp_x):
                max_x = temp_x
            test_x = temp_x
            f_test = fitness2(test_x)
            stop = False
        else:
            print("Reset")
            if stop:
                no_improvement = True
            stop = True
        print("Step: ",t,", Test: ",test_x, "Temp: ", temp_x)
        t += 1
     
    print("Start at ", start_x)    
    print("Iterations: ", t)
    print("Best x value: ", max_x)
    print("Best y value: ", fitness2(max_x))
    
    return max_x    

