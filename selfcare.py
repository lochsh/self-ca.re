import random as rnd


def count_lines(file_name):
    """Return number of lines in a file"""
    with open(file_name) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


def read_lines(file_name):
    """Read file line by line into list, return list"""
    words = []
    with open(file_name) as f:
        for line in f:
            words.append(line.rstrip())
    return words


def selfcare():
    """
    Return inspirational message ;o

    Reads a list of adjectives from adjectives.txt, and a list of nouns from
    nouns.txt.  A random entry from each is picked, and the two are combined to
    create an inspirational message:

    'You are a <adjective> <noun>'
    """
    # Count how many adjectives and nouns
    num_adj = count_lines('adjectives.txt')
    num_noun = count_lines('nouns.txt')

    # Randomly pick one adjective and one noun
    ind_adj = rnd.randint(0, num_adj - 1)
    ind_noun = rnd.randint(0, num_noun - 1)

    # Read adjectives and nouns
    adj = read_lines('adjectives.txt')
    nouns = read_lines('nouns.txt')
    return 'You are a%s %s' % (adj[ind_adj], nouns[ind_noun])


def main():
    print selfcare()

if __name__ == "__main__":
    main()
