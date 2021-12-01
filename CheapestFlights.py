"""
 Goal : Given n cities connected by some number of flights. We need to find the cheapest price
 to from from Source to Destination, with atmost K stops.
 Input : Array of flights [from, to, price]
 also Source, destination, K- number of stops allowed.
 Return -1 when no such path exists.

"""
from collections import defaultdict


def cheapest_flights(routes, source, destination, k):
    min_prices = defaultdict(lambda: float('inf'))
    # cost to reach source is 0
    min_prices[source] = 0

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


if __name__ == '__main__':
    routes = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    source, destination, stops = 0, 2, 1

    print(cheapest_flights(routes, source, destination, stops))
