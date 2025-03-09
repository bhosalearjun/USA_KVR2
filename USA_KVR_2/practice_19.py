def unique_values(value):
    lst=[]
    for val in value:
        if val not in lst:
            lst.append(val)
    return lst

word=input("enter the word:")

unique_chars=unique_values(word)

print(unique_chars)


