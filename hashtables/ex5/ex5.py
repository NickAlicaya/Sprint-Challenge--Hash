def finder(files, queries):
  
    cache = {}
    results = []
    
    for i in files:
       
        key = i.split('/')
        cache.setdefault(key[-1], []).append(i)    
  
    for j in queries:
        if 'nofile' in j:
            continue
        if j in cache:
            if len(cache[j]) > 1:
                for i in cache[j]:
                    results.append(i)
            else:
                results.append(cache[j][0])
        else:
            continue
    return results