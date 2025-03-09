while("python"):
    age = int(input("enter the age of citizen:"))

    if (age >= 18):
        print("{} age person is eligible to vote.".format(age))
        break
    print("{} age person is  not eligible to vote.".format(age))