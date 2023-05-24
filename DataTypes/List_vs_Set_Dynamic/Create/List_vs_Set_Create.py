def list_test():
    # Create an empty list
    my_list = []

    # Append 500000000 integers to the list
    for i in range(500000000):
        my_list.append(i)

    return my_list


def set_test():
    # Create an empty set
    my_set = set()

    # Add 500000000 integers to the set
    for i in range(500000000):
        my_set.add(i)

    return my_set


if __name__ == '__main__':
    #set_test()
    list_test()
