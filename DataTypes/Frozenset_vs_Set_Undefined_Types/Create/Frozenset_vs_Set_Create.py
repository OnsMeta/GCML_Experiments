def set_test():
    # Create an empty set
    my_set = set()

    # Add 500000000 integers to the set
    for i in range(500000000):
        my_set.add(i)

    return my_set


def frozenset_test():
    # Create a frozenset with 500000000 integers
    my_frozenset = frozenset(range(500000000))


if __name__ == '__main__':
    #frozenset_test()
    set_test()