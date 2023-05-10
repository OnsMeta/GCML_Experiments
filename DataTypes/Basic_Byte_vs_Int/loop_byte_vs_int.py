# Set the number of iterations
num_iterations = 1000000


# Test the byte data type
def byte_test():
    # Initialize an empty byte string
    a = b''
    # Loop through the number of iterations
    for i in range(num_iterations):
        # Concatenate a byte with value 2 to the byte string
        a += b'\x02'


# Test the integer data type
def int_test():
    # Initialize an integer variable with value 0
    a = 0
    # Loop through the number of iterations
    for i in range(num_iterations):
        # Add 2 to the integer variable
        a += 2


if __name__ == '__main__':
    byte_test()
    #int_test()