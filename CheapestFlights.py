"""
 Goal : Given n cities connected by some number of flights. We need to find the cheapest
 price to go from Source to Destination, with at-most K stops.
 Input : Array of flights [from, to, price]
 also Source, destination, K- number of stops allowed.
 Return -1 when no such path exists.

"""
from collections import defaultdict, deque


def cheapest_flights(routes, source, destination, K):
    """
    Bellman Ford calculates shortest path from a single source node to
    all other nodes in a weighted graph.
    min_prices - tracks current prices
    temp_prices - tracks prices of previous iteration.

    :param routes: list of available flights
    :param source: source of the trip
    :param destination: destination
    :param K: max num stops allowed
    :return: -1 or cheapest fare.
    O(K * number of routes)
    """
    min_prices = defaultdict(lambda: float('inf'))
    # cost to reach source is 0
    min_prices[source] = 0

    for i in range(K + 1):
        temp_prices = min_prices.copy()
        for src, dest, price in routes:
            if min_prices[src] == float('inf'):
                continue
            temp_prices[dest] = min(temp_prices[dest], temp_prices[src] + price)
        min_prices = temp_prices
    return -1 if min_prices[destination] == float('inf') else min_prices[destination]


def cheapest_flight_bfs(routes, source, destination, K):
    """
    A more intuitive search from source, traversing 1 level (a.k.a stop) at a time until the
    desired number of max stops allowed to reach destination.
    :param routes: src, dest flights.
    :param source: starting position
    :param destination: destination stop
    :param K: max number of stops allowed
    :return: cheapest fare if present , else -1
    Time Complexity : O(E * K)
    """
    # build the flight graph from given routes.
    adjList = defaultdict(list)
    for u, v, cost in routes:
        adjList[u].append([v, cost])

    q = deque([(source, 0)])

    stops, minPrice = 0, float('inf')

    while q:
        # to process neighbors level by level.
        # keeping track of stops
        for _ in range(len(q)):
            current, price = q.popleft()
            if current == destination:
                minPrice = min(minPrice, price)
                continue
            for neighbor in adjList[current]:
                dest_, price_ = neighbor
                if price + price_ > minPrice:
                    continue
                q.append((dest_, price + price_))
        if stops > K:
            break
        stops += 1

    return -1 if minPrice == float('inf') else minPrice


if __name__ == '__main__':
    routes = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    source, destination, stops = 0, 2, 1

    print(cheapest_flights(routes, source, destination, stops))
    print(cheapest_flight_bfs(routes, source, destination, stops))

    print(cheapest_flight_bfs(routes, source, destination, 0))
    print(cheapest_flights(routes, source, destination, 0))
