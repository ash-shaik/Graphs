"""
 We have an input of list of Airport codes (fixed 3 char codes), also a list of airport routes
 (from , to) and a start airport.
 Given this , we need to find the minimum number of new routes that will need to be added so
 as to reach all other airports (not necessarily directly)

 Identify it as a graph problem, with airports as vertices and routes as edges.
 Create a graph using the route info.

"""
from collections import defaultdict


def buildGraph(airports, routes):
    adjList = defaultdict(list)
    for from_, to in routes:
        adjList[from_].append(to)

    for airport in airports:
        if airport not in adjList:
            adjList[airport] = []


if __name__ == '__main__':
    airports = ["BGI"]
    routes = [["DSM", "ORD"]
              ]
    startingAirport = "LGA"
    buildGraph(airports, routes)
