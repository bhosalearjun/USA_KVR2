def getline():
    return input("enter the line:")

def getwordslength():
    line=getline()
    words=line.split()
    for word in words:
       print(f"{word}--------->{len(word)}")



getwordslength()