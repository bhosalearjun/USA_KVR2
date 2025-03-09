def get_line():
    return input("please enter the line:")

def reverse_the_line(ghar_line):
    words=ghar_line.split()
    print(words)
    print("-"*50)
    print(' '.join(words[::-1]))






line=get_line()

reverse_the_line(line)