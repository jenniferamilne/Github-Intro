# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import operator
import matplotlib.pyplot
import time

def distance_between(agents_row_a, agents_row_b):
    dist = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    return dist

#
random_seed = 1
random.seed(random_seed)

num_of_agents = 10
num_of_iterations = 100

agents = []
distances = []

# Make the agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])


# Move the agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):  
    
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


operator.itemgetter(1)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
#m = max(agents, key=operator.itemgetter(1))
#matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

distance = distance_between(agents[0], agents[1])
print(distance)

start = time.clock()

for agents_row_a in agents:
    for agents_row_b in agents:
        if (agents_row_a > agents_row_b):
            distance = distance_between(agents_row_a, agents_row_b)
            distances.append(distance)
            print(distance)
        
end = time.clock()
print ("time =" + str(end - start))

high = max(distances)
low = min(distances)

print ("max =" + str(high) +  " min =" + str(low))

