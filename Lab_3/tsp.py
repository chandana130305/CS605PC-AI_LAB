import random
import math
cities = [(0,0),(1,3),(4,3),(6,1)]
def distance(a, b):
    return math.dist(a, b)
def total_cost(route):
    cost = 0
    for i in range(len(route)):
        cost += distance(route[i], route[(i+1)%len(route)])
    return cost
def hill_climbing():
    current = cities[:]
    random.shuffle(current)
    while True:
        neighbors = []
        for i in range(len(current)):
            for j in range(i+1, len(current)):
                n = current[:]
                n[i], n[j] = n[j], n[i]
                neighbors.append(n)
        best = min(neighbors, key=total_cost)
        if total_cost(best) >= total_cost(current):
            print("Best route:", current)
            print("Cost:", total_cost(current))
            return
        current = best
hill_climbing()
