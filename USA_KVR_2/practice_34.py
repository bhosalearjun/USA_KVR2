def get_line():
    line=input("enter the line:")
    return line

def reverse_the_line(ghar_line):
    words=ghar_line.split()
    print(' '.join(reversed(words)))

    rev_line=' '.join(reversed (words))
    print(rev_line)




line=get_line()
reverse_the_line(line)