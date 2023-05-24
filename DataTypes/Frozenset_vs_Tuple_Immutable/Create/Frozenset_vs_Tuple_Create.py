

def tuple_test():
    # Create a tuple of 500000000 integers
    my_tuple = tuple(i for i in range(500000000))


def frozenset_test():
    # Create a frozenset with 500000000 integers
    my_frozenset = frozenset(range(500000000))


if __name__ == '__main__':
    tuple_test()
    #frozenset_test()

