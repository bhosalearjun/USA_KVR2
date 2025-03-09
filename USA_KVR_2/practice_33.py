def get_line():
    return input("enter the line:")

def reverse_the_line(ghar_line):
    words=ghar_line.split()
    print(words)
    rev_line=' '.join(reversed(words))
    print(rev_line)





line=get_line()
reverse_the_line(line)