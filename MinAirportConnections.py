"""
 We have an input of list of Airport codes (fixed 3 char codes), also a list of airport routes
 (from , to) and a start airport.
 Given this , we need to find the minimum number of new routes that will need to be added so
 as to reach all other airports (not necessarily directly)

 Identify it as a graph problem, with airports as vertices and routes as edges.
 1. Create a graph using the route info.
 2. Find airports that are unreachable from starting airport


"""
from collections import defaultdict, deque


def buildGraph(airports, routes):
    adjList = defaultdict(list)
    for from_, to in routes:
        adjList[from_].append(to)

    for airport in airports:
        if airport not in adjList:
            adjList[airport] = []
    return adjList


def dfs_unreachableAirports(Graph, startingAirport):
    unreachable = []
    visited = []

    q = deque()
    q.append(startingAirport)

    while q:
        current = q.popleft()
        visited.append(current)

        for neighbor in Graph[current]:
            if neighbor in visited:
                continue
            q.append(neighbor)

    for airport in Graph.keys():
        if airport not in visited:
            unreachable.append(airport)
    return unreachable


def scoreConnectivity(Graph, unreachableAirports, startingAirport):
    airportConnectivityDict = {}
    for airport in unreachableAirports:
        # Build out the airports they in turn connect.
        # dfs
        connectivity_list = dfs_connectivity(Graph, airport, startingAirport)
        airportConnectivityDict[airport] = connectivity_list
    return airportConnectivityDict


def dfs_connectivity(Graph, airport, startingAirport):
    """
    For the given airport, do a dfs and build reachability list.
    :param Graph:
    :param airport:
    :param startingAirport:
    :return: List of airports that are reachable from this input airport.
    """
    connectivity = []
    visited = []

    q = deque()
    q.append(airport)
    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.append(node)
        if node != airport and node != startingAirport:
            connectivity.append(node)

        for neighbor in Graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
    return connectivity


def findMinConnectionsForReachability(unreachableAirports
                                      , airportConnectivityDict):
    """
    Given the unreachableAirports list and the reachable connectivity,
    process airports out of unreachableAirports when a reachable connectivity is found
    :param unreachableAirports:
    :param airportConnectivityDict:
    :return: List of new connections to form to build reachability.
    """
    traverseList = sorted(airportConnectivityDict
                          , key=lambda a: len(airportConnectivityDict[a])
                          , reverse=True)
    # print(traverseList)

    numNewConnections = 0
    for airport in traverseList:
        if airport not in unreachableAirports:
            continue
        numNewConnections += 1
        for connection in airportConnectivityDict[airport]:
            unreachableAirports.remove(connection)
    return unreachableAirports


if __name__ == '__main__':
    airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN"
        , "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
    # print(len(airports))
    routes = [["DSM", "ORD"]
        , ["ORD", "BGI"], ["BGI", "LGA"], ["SIN", "CDG"], ["CDG", "SIN"], ["CDG", "BUD"], ["DEL", "DOH"]
        , ["DEL", "CDG"], ["TLV", "DEL"], ["EWR", "HND"], ["HND", "ICN"], ["HND", "JFK"], ["ICN", "JFK"]
        , ["JFK", "LGA"], ["EYW", "LHR"], ["LHR", "SFO"], ["SFO", "SAN"], ["SFO", "DSM"], ["SAN", "EYW"]
              ]
    startingAirport = "LGA"
    aGraph = buildGraph(airports, routes)
    unreachableAirports = dfs_unreachableAirports(aGraph, startingAirport)

    # print(len(unreachableAirports))
    airportConnectivityDict = scoreConnectivity(aGraph, unreachableAirports, startingAirport)
    reachabilityConnectionsList = findMinConnectionsForReachability(unreachableAirports, airportConnectivityDict)
    print(reachabilityConnectionsList)
