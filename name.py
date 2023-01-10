#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To apply the skills I've learned so far in the python course.
#
#

def start():
    print("Hello {}!".format(get_name()))


def get_name():
    name = input("What is your name?\n")
    return name





if __name__ == "__main__":
    start()
    

#######################################

def start():
    f_name = "Lucas"
    l_name = "English"
    age = 19
    gender = "Male
    get_info(f_name, l_name, age, gender)


def get_info(f_name, l_name, age, gender):
    print("my name is {} {}, I am a {} year old {}".format(f_name, l_name, age, gender)
          


if __name__ == "__main__":
    start()
