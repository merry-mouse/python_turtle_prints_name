""" asks user to print the array of numbers(integers or floats) and returns the second largest from it. 
    if user put string as an input/empty list/list with identical values, the program print an error message. """
    
    if __name__ == '__main__':
    try:
        list_arr = list(map(float, input("Print an array of numbers (ex: 1 2 3 4 3):\n").split()))
    except ValueError:
        print("There is a string in your input. Array must include integers only.")
    # counting the length of the input array, we need it to be at least 2 characters long
    length_of_list = len(list_arr)
    # if the length is 0 or 1 character only, we want to finish the program and print the rules
    # otherwise if the length is at least 2 characters, we continue
    if length_of_list == 0 or length_of_list == 1:
        print("the length of the array should be at least 2 characters")
    else:
        # changing type to a list
        # sorting the list
        sorted_arr = sorted(list_arr)
        # finding the max value
        try:
            max_n = max(list_arr)
            # removing the known maximum and thus making the second max new max
            i = range(0, len(list_arr))
            for number in i:
                for char in sorted_arr:
                    if char == max_n:
                        sorted_arr.remove(char)
            print("The second largest is: {}".format(max(sorted_arr)))
        except ValueError:
            print("Numbers in your array are the same and it is impossible to find the second largest. You can try "
                  "again with a different array. ")
