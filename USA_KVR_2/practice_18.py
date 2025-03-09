def uniquevalues(value):
    lst=[]
    for val in value:
        if val not in lst:
            lst.append(val)

    return lst

word=input("enter the word:")

unk_val=uniquevalues(word)

print("the given word is {}".format(word))


print("the uniques values are {}".format(unk_val))
