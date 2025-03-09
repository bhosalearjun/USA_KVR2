while(True):
    name=input("enter the name:")
    name_words=name.split()
    is_alpha=True
    for word in name_words:
        if(not word.isalpha()):
            is_alpha=False
            break
    if(is_alpha):
        print("{} is valid name".format(name))
        break
    else:
        print("{} is invalid name".format(name))


