#!/usr/bin/python3
def char_count(str):
    char_list = set(str)
    for char in char_list:
        print(char,str.count(char))
if __name__ == '__main__':
    s = input("enter a string:")
    char_count(s)

