def circle_of_numbers(n, first_number):
    """ Finds the number which is in the radial opposite position to the first_number in a circle.

    :param n: size of the circle
    :type n: int
    :param first_number: the start number used to find the radial opposite number
    :type first_number: int
    :return: the number which is radially opposite of first_number
    :rtype: int
    """
    numbers = list(range(n))
    half = int(n / 2)

    first_num_idx = numbers.index(first_number)
    if first_num_idx + half > len(numbers) - 1:
        return numbers[first_num_idx - half]
    return numbers[first_num_idx + half]
