import random


def read_lines(file_name):
    """Return list where each entry is a line from file"""
    with open(file_name) as f:
        return f.read().splitlines()


def selfcare():
    """
    Return inspirational message ;o

    Reads a list of adjectives from adjectives.txt, and a list of nouns from
    nouns.txt.  A random entry from each is picked, and the two are combined to
    create an inspirational message:

    'You are a <adjective> <noun>'
    """
    adjs = read_lines('adjectives.txt')
    nouns = read_lines('nouns.txt')
    return 'You are a{0} {1}'.format(random.choice(adjs),
                                     random.choice(nouns))


def main():
    print(selfcare())

if __name__ == "__main__":
    main()
