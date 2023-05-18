#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()

    for i in new_dir.keys():
        new_dir[i] *= 2

    return (new_dir)
	
