#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = []
    # loop through the tickets and add to cache.
    # set the key = source, value = destination
    for i in tickets:
        cache[i.source] = i.destination
    # The starting ticket has the key 'NONE'    
    current_value = cache['NONE']
    # while length of route is less than number of tickets
    while len(route) < length:
        # first attaches ticket with key=None and value =destination 
        route.append(current_value)
        # pointer changes to item in cache at index = current_value
        # which changes the cache current index to the value of the previous one
        current_value = cache[current_value]
    return route   
   




  



