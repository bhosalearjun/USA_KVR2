def get_line():
    return input("enter the line:")

def count_of_characters(ghar_line):
    words=ghar_line.split()
    print(words)
    print('-' * 50)
    for word in words:
        print("{}-------->{}".format(word,len(word)))

    

line=get_line()

count_of_characters(line)