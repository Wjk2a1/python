###############################################################
# FILE: oneliners.py
# Description:
# A set of functions that perform various tasks written in
# as few lines as possible.
################################################################

import re
import string, random
from itertools import accumulate, repeat

def is_two_palindrome(str):
    '''Checks if a given string is a two_palindrome and
       returns true if so, false otherwise.'''
    len1 = len(str)//2
    if len(str) % 2 == 0: return (str[:len1] == str[:len1][::-1]) and\
                                 (str[len1:] == str[len1:][::-1])
    return (str[:len1] == str[:len1][::-1]) and\
           (str[len1+1:] == str[len1+1:][::-1])


def uni_sort(lst1, lst2):
    '''This function receives two lists of integers, merges
       them with no duplicates and sorts them.'''
    new_list = [num for i, num in enumerate(lst1+lst2)\
                if num not in (lst1+lst2)[i+1:]]
    new_list.sort()
    return new_list


def dot_product(vector1, vector2):
    '''This function receives two vectors and
       returns their dot product.'''
    return sum(a*b for a,b in zip(vector1, vector2))


def list_intersection(lst1, lst2):
    '''This function receives two lists of integers
       and returns their sorted intersection.'''
    return sorted(set(lst1).intersection(lst2))


def list_difference(lst1, lst2):
    '''This function receives two lists of integers
       and returns the numbers that belong only to one
       of the lists.'''
    return sorted([num for num in set(lst1 + lst2) \
                   if num not in lst1 or num not in lst2])


def random_string(n):
    '''This function receives a number 'n' and
       generates a random string with the length
       of 'n'.'''
    return ''.join(random.choice(string.ascii_lowercase) for x in range(n))


def word_mapper(str):
    '''This function returns a dictionary mapping from the words
       in the input text 'str' to their number of appearances.'''
    a = re.split('[\W_]+', str.lower())
    return dict(zip(filter(None, a), [a.count(n) for n in filter(None,a)]))



def gimme_a_value(func, x0):
    '''This is a generator that receives a function and a
       starting point x0. It computes the values of the function
       and return it.'''
    while True:
        yield x0
        x0 = func(x0)


def gimme_a_genexp(func, x0):
    '''This function returns a generator expression using the
       given function.'''
    return accumulate(repeat(x0), lambda x0, gimme_a_genexp: func(x0))



