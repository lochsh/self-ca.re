#!/usr/bin/env/python

import random as rnd

"""
Function to count lines in a file
"""
def count_lines(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

"""
Read file line by line into list
"""
def read_lines(fname):
    words = []
    with open(fname) as f:
        for line in f:
            words.append(line.rstrip())
    return words

"""
Make inspirational message ;o
"""
def selfcare():
    #Count how many adjectives and nouns
    A = count_lines('adjectives.txt')
    N = count_lines('nouns.txt')

    #Randomly pick one adjective and one noun
    a = rnd.randint(0,A-1)
    n = rnd.randint(0,N-1)

    #Read adjectives and nouns
    adj = read_lines('adjectives.txt')
    nouns = read_lines('nouns.txt')

    #;o  quick and dirty line breaks as I haven't got vertical alignment to work in CSS yet :'(
    if len(adj[a]) < 7:
        message = '<br> <br> <br> <br>You are a' + adj[a] + '<br> <br>'  + nouns[n]
    elif len(adj[a] + nouns[n]) < 12:
        message = '<br> <br> <br> <br>You are<br> <br>a' + adj[a] + ' '  + nouns[n]
    else:
        message = '<br> <br> <br>You are<br> <br>a' + adj[a] + '<br> <br>' + nouns[n]
    return message

def main():
    print selfcare()

if __name__ == "__main__":
    main()
