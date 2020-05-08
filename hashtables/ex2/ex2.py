#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = []
    for i in tickets:
        cache[i.source] = i.destination
        # print(cache)
    current_value = cache['NONE']
    while len(route) < length:
        route.append(current_value)
        current_value = cache[current_value]
    return route   




  



