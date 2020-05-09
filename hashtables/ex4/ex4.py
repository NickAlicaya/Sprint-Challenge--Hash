def has_negatives(a):

    pairs = []
    storage = {}

    # iterate through array
    # store each item in array as key in dictionary with No value
    # iterate through array and look for negative numbers
    # multiply negative number by -1 and see if that value is in dictionary
    #     if it is then append to pairs list as an absolute number so we dont get a negative result

    for num in a:
        if num not in storage:
            storage[num] = None
    for num in a:
        if num < 0:
            if (num * -1) in storage:
                pairs.append(abs(num))    
    return pairs

if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))


    
