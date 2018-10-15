# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

# Set up variables.
y0 = random.randint(0,99)
x0 = random.randint(0,99)


#Random walk one step.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

print(y0)


# Move y0 randomly
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

# Move x0 randomly
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)





# Make y1 and x1 = 50

y1 = 50
x1 = 50

# Move y1 randomly
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

# Move x1 randomly
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)


# answer = Pythagorian distance between y0,x0 and y1,x1
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)