import random
import numpy as np

# Set the random seed to a specific value (e.g., 42)
np.random.seed(42)

# Create an array with 100 random elements ranging from 0 to 499999999 in order to access the same random values
my_array = np.random.randint(0, 50000000, size=100)

def tuple_test():
    # Create a tuple of 500000000 integers
    my_tuple = tuple(i for i in range(50000000))

    # Select a random element from the tuple and find it
    for i in range(100):
        if my_array[i] in my_tuple:
            pass


def frozenset_test():
    # Create a tuple of 500000000 integers
    my_frozenset = frozenset(range(50000000))
    # Access 100 random elements from the frozenset
    for i in range(100):
        if my_array[i] in my_frozenset:
            pass


if __name__ == '__main__':
    #frozenset_test()
    tuple_test()