def get_line():
    return input("enter the line:")


def reverse_the_string(ghar_line):
    print("-"*50)
    print(ghar_line)
    print("-"*50)
    words=ghar_line.split()
    print(words)
    print(' '.join(words[::-1]))
    print("-"*50)
    rev_words=words[::-1]
    print(rev_words)
    print(' '.join(rev_words))









line=get_line()
reverse_the_string(line)