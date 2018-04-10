# coding: utf-8

def change(some_list):
    some_list[1] = 4

x = [1,2,3]
change(x)
print(x) # Prints out [1,4,3]
