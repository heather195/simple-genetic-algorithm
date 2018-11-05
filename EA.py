#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 00:53:31 2018

@author: heathercraddock
"""

import numpy as np
import math 
import matplotlib.pyplot as plt

pop_size = 8
initial_pop = np.random.randint(2,size=(pop_size,12))
P = np.copy(initial_pop)
pc = 0.6
pm = 0.02
target = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]

"""
def print_pop_members(matrix):
    member_width = 3
    member_height = 4
    member = range(member_width*member_height)
    member = np.reshape(member,(member_height,member_width))
    
    for x in range(pop_size):
        line = matrix[x]
        j = 0
        i = 0
        for j in range(member_width):
            for k in range(member_height):
                member[k,j] = line[i]
                i = i + 1
        print(member)
        print(" ")
        # Double check this for bugs
"""


def crossover(p1, p2):
    #choose an index for the crossover split and initialise children
    index = np.random.randint(0,12)
    c1 = [] 
    c2 = []
    
    #print("crossover ",p1," & ",p2," @ ",index)
    #create a child from both parents using the split
    c1[0:index]=p1[0:index]
    c1[index::]=p2[index::]
    #create the second child splitting the c
    c2[0:index]=p2[0:index]
    c2[index::]=p1[index::]
    
    return c1, c2

def reproduce(matrix, pc):
    half_pop = int(pop_size/2)
    temp = np.random.uniform(0,1,(half_pop))
    #print(temp)
    M = np.copy(matrix)
    x, y = 0, 0
    while(x < pop_size): 
        if(temp[y]<pc):
            M[x], M[x+1] = crossover(M[x],M[x+1])
        y = y + 1
        x = x + 2
        
    return M

    
def mutate(matrix, pm):
    M = np.copy(matrix)
    #print(np.matrix(M))
    num_positions = M.shape[0] * M.shape[1]
    num_to_switch = int(num_positions*pm)
    indicesx = np.random.randint(0, high = M.shape[0] - 1, size = num_to_switch)
    indicesy = np.random.randint(0, high = M.shape[1] - 1, size = num_to_switch)
    for i in range(num_to_switch):
        #print("Mutate at ", indicesy[i], ",", indicesx[i])
        if(M[indicesx[i],indicesy[i]] == 1):
            M[indicesx[i],indicesy[i]] = 0
        elif(M[indicesx[i],indicesy[i]] == 0):
            M[indicesx[i],indicesy[i]] = 1
    #print(np.matrix(M))
    return M

def fitness(matrix, target):
    fit_found = False
    line_fit = [0,0,0,0,0,0,0,0]
    for x in range(0, pop_size):
        line_fit[x] = np.sum(matrix[x] == target)
        if(line_fit[x] == 12):
            fit_found = True
    return line_fit, fit_found


def spin(pop_size):
    num = np.random.randint(361, size = pop_size)
    return num

def selection(matrix, line_fit):
    M = np.copy(matrix)
    roulette = [0,0,0,0,0,0,0,0]
    roulette[0] = line_fit[0]*(360/np.sum(line_fit))
    for y in range(1, pop_size):
        roulette[y] = line_fit[y]*(360/np.sum(line_fit)) + roulette[y-1]
    for z in range(0, pop_size):
        roulette[z] = math.ceil(roulette[z])
    
    spin_values = spin(pop_size)
    selected_matrix = np.copy(M)
    section_val = 0
    section_found = False
    
    for i in range(0, pop_size):
        x = 0
        while not section_found:
            if spin_values[i]<= roulette[x]:
                #print("found section", x)
                section_found = True
                section_val = x
            else:
                x = x + 1
        selected_matrix[i] = M[section_val]
        section_found = False

    return selected_matrix

def graphPop (matrix):
    plt.title('Population')
    plt.imshow(matrix)
    plt.show()

def run(select, pc, pm, target, fit, total_gens):
    select2 = np.copy(select)
    x = 0
    run_num = list()
    max_fitness = list()
    
    while x < total_gens:
        run_num.append(x)
        max_fitness.append(max(fit[0]))
        #graphPop(select2)
        if fit[1]:
            #print_pop_members(select)
            #print("Fit child found in generation ", x)
            #return x, run_num, max_fitness
            return x, select2
        select2 = reproduce(select2, pc)
        select2 = mutate(select2, pm)
        fit = fitness(select2, target)
        select2 = selection(select2,fit[0])
        x = x+1
    if fit[1] == False:
        return -1, select2
        #print(select)
        #print(" ")



fit = fitness(P, target)
select = selection(P,fit[0])
matr = np.copy(select)
runtimes, num_gens, count = 5, 2000, 0
fit_child_found = 0
child_found_gen, lowest_gen, highest_gen, total_gen,avg_gen = 0, 1000000, 0, 0, 0

print("Initial Population")
graphPop(initial_pop)

for y in range(0, runtimes):
    child_found_gen = run(select, pc, pm, target, fit, num_gens)
    if child_found_gen[0] > 0:
        fit_child_found = fit_child_found + 1
        total_gen = total_gen + child_found_gen[0]
        if child_found_gen[0] < lowest_gen:
            lowest_gen = child_found_gen[0]
        if child_found_gen[0] > highest_gen:
            highest_gen = child_found_gen[0]
        count = count + 1
        print("Run: ",y+1)
        graphPop(child_found_gen[1])
if count > 0:        
    avg_gen = total_gen / count
else:
    avg_gen = "NO CHILDREN FOUND"

print("In ",runtimes," runs, going until a fit child was found or ",num_gens," generations:")
print("Quickest child found: Generation ", lowest_gen)
print("Slowest child found: Generation ", highest_gen)
print("Average speed of child found: Generation ", avg_gen)
print("Fit child found ",fit_child_found,"/",runtimes," times")



#print(select)
#print(" ")


#print(select)    
#print_pop_members(select)



        
