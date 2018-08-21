from numigi_tests import remove_duplicates, remove_duplicates_better


def test_remove_duplicates():
    assert sorted([1, 2, 3, 4, 5]) == sorted(remove_duplicates([1, 1, 2, 2, 2, 3, 4, 5, 5]))
    assert sorted(["Hello", "There"]) == sorted(remove_duplicates(["Hello", "Hello", "There", "There"]))


def test_remove_duplicates_better():
    assert sorted([10, 20, 30, 40, 50]) == sorted(remove_duplicates_better([10, 10, 20, 20, 20, 30, 40, 50, 50]))
    assert sorted(["Soul", "Reality", "Time", "Space", "Power", "Mind", "Stone"]) == sorted(remove_duplicates_better(
        ["Soul", "Stone", "Reality", "Stone", "Time", "Stone", "Space", "Stone", "Power", "Stone", "Mind", "Stone"]))


def test_that_empty_list_returns_nothing():
    assert [] == remove_duplicates()
    assert [] == remove_duplicates_better()
