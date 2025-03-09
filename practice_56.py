def get_line():
    line=input("enter the line:")
    return line

def revese_the_string(ghar_line):
    words=ghar_line.split()
    print(words)
    print("-"*50)
    print(' '.join(words[::-1]))
    print("-"*50)
    rev_words=words[::-1]
    print(rev_words)
    print(' '.join(rev_words))






line=get_line()
revese_the_string(line)