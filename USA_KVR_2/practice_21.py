def unique_characters(value):
    lst=[]
    for val in value:
        if val not in lst:
            lst.append(val)

    return lst




word=input("enter the word:")
result=unique_characters(word)


print(result)
print("number of character=",len(result))

print("unique word=","".join(result))