def get_indices_of_item_weights(weights, length, limit):

    wt_dict = {}
    for i in range(len(weights)):
        if weights[i] not in wt_dict:
            wt_dict[weights[i]] = [i]
        else:
            wt_dict[weights[i]] += [i]
    
    for wt in weights:
        
        if limit - wt in wt_dict:
            if wt == limit - wt:
                return [wt_dict[wt][1], wt_dict[wt][0]]
            if wt > wt_dict[limit-wt][0]:
                return [wt_dict[limit-wt][0], wt_dict[wt][0]]
            else:
                return [wt_dict[wt][0]. wt_dict[limit-wt][0]]

    return None


