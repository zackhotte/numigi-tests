# Numigi Tests

Answers to the five test questions from Numigi.

## Test Questions & Answers

All 5 Numigi test questions have been answered and completed and each can be found in their own packages within the
numigi_tests package. Each test question (except test2) has a corresponding unit test associated with it (please see the 
"Running the tests" section)
 
### Test1: circle_of_numbers

**Question**

Consider integer numbers from 0 to n 1
written down along the circle in such a way that the distance between any two neighboring numbers is equal 
(note that 0 and n - 1 are neighboring, too).<br><br>
Given n and first_number, find the number which is written in the radially opposite position to
first_number.

**Answer**

You can import the method circle_of_numbers from the numigi_tests package and feel free to test it out

```
>>> from numigi_tests import circle_of_numbers
>>> circle_of_numbers(n=10, n=2)
7
```

*Please feel free to explore numigi_tests.test1 package to review the code.*

### Test2: Utilisation des design patterns

**Question**

Donner des exemples de classes que le développeur a écrite qui implémente un design
pattern et expliquer pourquoi ce pattern a été utilisé plutôt qu’un autre.

**Answer**

Please read the [README.md](https://github.com/zackhotte/numigi-tests/numigi_tests/test2/README.md) document inside the 
package numigi_tests.test2.

### Test3: Décorateur

**Question**

Écrire un décorateur `redirect_exception` qui redirige un type d’exception vers un autre type.

**Answer**

First import the redirect_exception from the numigi_tests package
```
from numigi_tests import redirect_exception
```

Then, feel free to test out the decorator on custom functions that will throw exceptions
```
@redirect_exception(TypeError, ValueError)
def add_int_and_string():
    return 1 + "2"
    
add_int_and_string()
```

The result should output a ValueError instead of a typical TypeError

*Please feel free to explore numigi_tests.test3 package to review the code.*

### Test4: Duplicates

**Question**

Commenter la fonction suivante pour mettre en avant ses faiblesses et proposer des
améliorations.

**Answer**

Please explore the package *numigi_tests.test4* and review my notes for each function, which can found just above
the main function and the improved version of the function.

### Test5: 99 Bottles of beer

**Question**

Nous voudrions que tu écrives un script qui reproduit efficacement les paroles de la chanson “99 bottles of beers”.

**Answer**

First import the ninety_nine_bottles_of_beer from the numigi_tests package and then run the method to get all the lyrics
from the song “99 bottles of beers”
```
>> from numigi_tests import ninety_nine_bottles_of_beer
>> ninety_nine_bottles_of_beer()
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
...
2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
```

*Please feel free to explore numigi_tests.test5 package to review the code.*

## Running the tests

First, setup you Virtualenv environment
```
python -m venv env
source env/bin/activate
```

Then, install all the dependencies
```
pip install -r requirements.txt
```

Afterwards, simply run Pytest to ensure that all the tests pass

```
pytest
```

## Author

**Zachary Hotte** - [zackhotte](https://github.com/zackhotte)
