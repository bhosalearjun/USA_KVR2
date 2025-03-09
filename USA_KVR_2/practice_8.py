while(True):
    name=input("enter your name:")
    name_words=name.split()
    if len(name_words)==0:
        print("please enter name and not a space")
    else:


        is_word=True
        for word in name_words:
            if (not word.isalpha()):
                is_word=False
                break
        if(is_word):
            print("{} given word is valid".format(name))
            break
        else:
            print("given {} word is invalid".format(name))
