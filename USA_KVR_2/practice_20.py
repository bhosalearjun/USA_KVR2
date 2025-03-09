def unique_values(value):
    lst=[]
    for val in value:
        if val not in lst:
            lst.append(val)
    print(lst)
    return lst




print(unique_values("missippi"))

