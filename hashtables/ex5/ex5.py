def finder(files, queries):
  
    cache = {}
    results = []
    
    for i in files:
        # loops through files removes the backslash 
        key = i.split('/')
        # if the key is in the cache it will return value if not it will add the last item as the key
        cache.setdefault(key[-1], []).append(i)    
  
    for j in queries:
        # skip if string contains nofile
        if 'nofile' in j:
            continue
        # if the string is found in cache    
        if j in cache:
            if len(cache[j]) > 1:
                for i in cache[j]:
                    results.append(i)
            else:
                results.append(cache[j][0])
        else:
            continue
    return results

  