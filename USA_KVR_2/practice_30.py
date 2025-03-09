def get_a_line():
    return input("enter the line:")



def char_count_in_each_word_in_line(ghar_line):
    print('-'*50)
    words=ghar_line.split()
    print(words,type(words))
    print('-' * 50)
    for word in words:
        print(f"{word} --------------> {len(word)}")


line=get_a_line()

char_count_in_each_word_in_line(line)