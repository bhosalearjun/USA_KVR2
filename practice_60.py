def get_line():
    return input("enter the line:")

def display_reverse_the_string(ghar_line):
    words=line.split()
    rev_string=words[::-1]
    print(rev_string)
    print(' '.join(rev_string))






line=get_line()
display_reverse_the_string(line)