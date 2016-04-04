import random


def count_lines(file_name):
    """Return number of lines in a file"""
    with open(file_name) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


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
    num_adj = count_lines('adjectives.txt')
    num_noun = count_lines('nouns.txt')

    ind_adj = random.randint(0, num_adj - 1)
    ind_noun = random.randint(0, num_noun - 1)

    adj = read_lines('adjectives.txt')
    nouns = read_lines('nouns.txt')
    return 'You are a%s %s' % (adj[ind_adj], nouns[ind_noun])


def main():
    print selfcare()

if __name__ == "__main__":
    main()
