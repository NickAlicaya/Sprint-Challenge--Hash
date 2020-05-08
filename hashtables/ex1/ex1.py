from hashtable import *


def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """   

    ht = HashTable(10)
    if length == 1:
        return None
    for i in range(length):
        ht.put(weights[i], i)

    for i in range(0, length):
        difference = limit - weights[i]
        result = ht.get(difference)
        if result is not None:
            return(result, i)

    if difference is not None:
        if difference >= i:
            return (difference, i)
        else:
            return (i, difference)
    return None    

