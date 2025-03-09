def get_line():
    return input("enter the line whose words to reverse:")

def Reverse_Each_Words_Characters(ghar_line):
    words=ghar_line.split()
    reverse_characters=[]
    for word in words:
        rev_word=word[::-1]
        print(rev_word)
        reverse_characters.append(rev_word)
    print(reverse_characters)

    print(' '.join(reverse_characters ))








line=get_line()
Reverse_Each_Words_Characters(line)