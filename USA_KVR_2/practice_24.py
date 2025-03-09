def getline():
    line=input("enter the line:")
    return line

def getwordslenght(line):
    words=line.split()
    for word in words:
        print("{}--------->{}".format(word,len(word)))


linesss=getline()
getwordslenght(linesss)