def get_line():
    return input("enter the line:")

def disp_number_of_characters_in_each_word(ghar_line):
    print(ghar_line)
    print("-"*60)
    words=ghar_line.split()
    print(words,type(words))
    print("-"*60)
    for word in words:
        print(f"{word}---->{len(word)}")







line=get_line()

disp_number_of_characters_in_each_word(line)