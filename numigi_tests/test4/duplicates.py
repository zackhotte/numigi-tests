"""
NOTES for remove_duplicates:

Iterating over one item at a time and calling count on each item can be computationally expensive. You have to iterate
over each item, which will take `n` time, with `n` being equal to the size of the list, then you call .count()
on each item, which has to reiterate over the list of n items again. Computationally, this looks like it would
take about O(n^2) time, which is quite slow.
"""


def remove_duplicates(source=[]) -> list:
    """Remove all the duplicates from the given flat list.

    :param list source: list to "purge"
    :return: list without duplicates
    :rtype: list
    """
    for item in source:
        if source.count(item) > 1:
            source.remove(item)
    return source


"""
NOTES for remove_duplicates_better:

This method is more efficient for removing duplicates as you first create a set and then convert it to a list. Creating
a set should have an efficiency of at most O(n) time (with n being equal to the size of the list), which is faster than 
the method remove_duplicates(). Also, this method is much cleaner and easier to read, making an overall more efficient 
algorithm.
"""


def remove_duplicates_better(source=[]) -> list:
    """Remove all the duplicates from the given flat list.

    :param list source: list to "purge"
    :return: list without duplicates
    :rtype: list
    """
    return list(set(source))
