def get_line():
    return (input("enter a line:"))

def get_chaars_count(line_ghar):
    words=line_ghar.split()
    for word in words:
        print("{}--------->{}".format(word,len(word)))








line=get_line()
get_chaars_count(line)