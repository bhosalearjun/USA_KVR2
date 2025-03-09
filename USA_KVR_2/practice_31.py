def get_line():
    """Gets a line of input from the user."""
    return input("Enter a line: ")

def count_chars_in_words(line):
    """Counts the characters in each word of a given line."""
    words = line.split()
    for word in words:
        print(f"{word} --> {len(word)}")

def main():
    line = get_line()
    count_chars_in_words(line)

if __name__ == "__main__":
    main()