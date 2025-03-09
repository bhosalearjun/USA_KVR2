def get_line():
    return input("enter the line:")

def reverse_the_line(ghar_line):
    words=ghar_line.split()
    reverse_line=' '.join(reversed(words))
    print("reversed line=",reverse_line)

    print('rev_line='," ".join(reversed(words)))







line=get_line()
reverse_the_line(line)