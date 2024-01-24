#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == word else word for word in my_list]
