def get_line():
    return input("enter the line:")

def reverse_the_characters_of_word_in_Line(ghar_line):
    words=ghar_line.split()
    print(words)
    print("-"*50)
    print(' '.join(words[::-1]))






line= get_line()
reverse_the_characters_of_word_in_Line(line)