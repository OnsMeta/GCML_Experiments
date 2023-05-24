import numpy as np

# Set the random seed to a specific value (e.g., 42)
np.random.seed(42)

# Create an array with 100 random elements ranging from 0 to 499999999 in order to access the same elements
my_array = np.random.randint(0, 50000000, size=100)


def list_test():
    # Create an empty list
    my_list = []

    # Append 500000000 integers to the list
    for i in range(50000000):
        my_list.append(i)

    for i in range(100):
        # Select a random element from the list and find it
        if my_array[i] in my_list:
            pass


def set_test():
    # Create a set of 500000000 integers
    my_set = set(i for i in range(50000000))

    for i in range(100):
        # Select a random element from the set and find it
        if my_array[i] in my_set:
            pass


if __name__ == '__main__':
    #list_test()
    set_test()