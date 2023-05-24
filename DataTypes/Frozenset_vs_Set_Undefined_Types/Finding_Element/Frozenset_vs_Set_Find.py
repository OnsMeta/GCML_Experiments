import random
import numpy as np

# Set the random seed to a specific value (e.g., 42)
np.random.seed(42)

# Create an array with 1000 random elements ranging from 0 to 499999999 in access the same values
my_array = np.random.randint(0, 500000000, size=1000)

def frozenset_test():
    # Create a frozenset of 500000000 integers
    my_frozenset = frozenset(range(500000000))
    # Access 1000 random elements from the frozenset
    for i in range(1000):
        if my_array[i] in my_frozenset:
            pass

def set_test():
    # Create a set of 500000000 integers
    my_set = set(i for i in range(500000000))

    for i in range(1000):
        # Select a random element from the set and find it
        if my_array[i] in my_set:
            pass


if __name__ == '__main__':
    frozenset_test()
    #set_test()
