import numpy as np

# Set the random seed to a specific value (e.g., 42)
np.random.seed(42)

# Create an array with 10000 random elements ranging from 0 to 499999999 in order to always access the same random numbers
my_array = np.random.randint(0, 500000000, size=10000)


def list_test():
    # Create an empty list
    my_list = []

    # Append 500000000 integers to the list
    for i in range(500000000):
        my_list.append(i)

    # Access 10000 random elements from the list
    for i in range(10000):
        random_element = my_list[my_array[i]]


def tuple_test():
    # Create a tuple of 500000000 integers
    my_tuple = tuple(i for i in range(500000000))

    # Access 10000 random elements from the tuple
    for i in range(10000):
        random_element = my_tuple[my_array[i]]


if __name__ == '__main__':
    list_test()
    #tuple_test()