"""
 Goal : Given n cities connected by some number of flights. We need to find the cheapest price
 to from from Source to Destination, with atmost K stops.
 Input : Array of flights [from, to, price]
 also Source, destination, K- number of stops allowed.
 Return -1 when no such path exists.

"""
from collections import defaultdict


def cheapest_flights(routes, source, destination, k):
    min_prices = defaultdict(lambda x: float('inf'))

    # cost to reach source is 0
    min_prices[source] = 0

    # Mimic BFS to see what stops we can reach, with 1 stop.
    # continue this for K stops.
    # ignoring cross edges.
    for i in range(k + 1):
        temp_prices = min_prices.copy()
        for src, dest, price in routes:
            if min_prices[src] == float('inf'):
                continue
            newPrice = min_prices[src] + price
            oldPrice = temp_prices[dest]
            if newPrice < oldPrice:
                temp_prices[dest] = newPrice
        min_prices = temp_prices
    return -1 if min_prices[destination] == float('inf') else min_prices[destination]
