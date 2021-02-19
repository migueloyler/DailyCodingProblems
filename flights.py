'''
You are given a huge list of airline ticket prices between different cities around the world on a given day. 
These are all direct flights. Each element in the list has the format (source_city, destination, price).

Consider a user who is willing to take up to k connections from their origin city A to their destination B.
 Find the cheapest fare possible for this journey and print the itinerary for that journey.

For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are as follows:

[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]

Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.
'''
class Solution: 

    def __init__(self):
        self.solution = []

    def flight(self, arr, src, dest, c):
        preprocess = {}
        for i in arr:
            if i[0] in preprocess:
                preprocess[i[0]].append((i[1],i[2]))
            else:
                preprocess[i[0]] = [(i[1],i[2])]
        for i in preprocess.keys():
            preprocess[i] = sorted(preprocess[i], key= lambda x: x[1])
        
        def flight_helper(src, dest, cur_cost, connections, path, preprocess):
            path.append(src)
            if connections < 0:
                return 100000000000000
            if src == dest:
                print(path)
                print(cur_cost)
                return cur_cost
            if src in preprocess:
                for i in preprocess[src]:
                    self.solution.append(flight_helper(i[0],dest,cur_cost+i[1],connections-1, path,preprocess))
            return min(self.solution)

        return flight_helper(src, dest, 0, c, [], preprocess)

arr = [
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]

solution = Solution()
solution.flight(arr, 'JFK', 'LAX', 3)