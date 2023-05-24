# Create a list that contains 700000000 elements
def list_test():
    # Create an empty list
    my_list = []

    # Append 700000000 integers to the list
    for i in range(700000000):
        my_list.append(i)


def tuple_test():
    # Create a tuple of 700000000 integers
    my_tuple = tuple(i for i in range(700000000))


if __name__ == '__main__':
    tuple_test()
    # list_test()
