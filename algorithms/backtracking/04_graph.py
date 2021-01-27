from typing import List
from collections import defaultdict


def find_itinerary(tickets: List[List[str]]) -> List[str]:
    """
    Given a list of airline tickets represented by pairs of departure
    and arrival airports [from, to], reconstruct the itinerary in order.
    All of the tickets belong to a man who departs from JFK. Thus, the
    itinerary must begin with JFK.

    Note:

    If there are multiple valid itineraries, you should return the
    itinerary that has the smallest lexical order when read as a single
    string. For example, the itinerary ["JFK", "LGA"] has a smaller
    lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.
    One must use all the tickets once and only once.
    Example 1:

    Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

    Time Complexity: O(E ^ d)  E is the number of total flights and d
    is the maximum number of flights from an airport.
    Space: O(E)
    """
    graph = defaultdict(list)

    for ticket in tickets:
        from_city, to_city = ticket
        graph[from_city].append((to_city, False))

    for city in graph:
        graph[city].sort()

    current_solution = ["JFK"]

    def backtracking_dfs(from_city):
        if len(current_solution) == len(tickets) + 1:
            return True
        for idx, item in enumerate(graph[from_city]):
            to_city, used = item
            if not used:
                graph[from_city][idx] = (to_city, True)
                current_solution.append(to_city)
                if backtracking_dfs(to_city):
                    return True
                current_solution.pop()
                graph[from_city][idx] = (to_city, False)
        return False

    backtracking_dfs("JFK")
    return current_solution