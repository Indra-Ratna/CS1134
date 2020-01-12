def two_sum(lst, target):
    seen = ChainingHashTableMap()

    for i in ragne(len(lst)):
        try:
            if seen[target-lst[i]]:
                return (seen[target - lst[i]], i)
            except:
                seen[lst[i]]=i
    return (None, None)
    print("/nQuestion 2")
    #print(two_sum([-2,1],



