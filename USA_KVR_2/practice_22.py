def getline():
    line=input("enter the line:")
    return line



def getwords_length(line):
    words=line.split()
    for word in words:
        print("{} ---------->{}".format(word,len(word)))



lines=getline()

getwords_length(lines)


