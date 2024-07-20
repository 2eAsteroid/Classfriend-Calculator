import sys
import fractions
import itertools as itools
import functools as ftools
from operator import add

def calculate_probability(class_distribution: list[int]) -> int:
    total_seats = ftools.reduce(add, class_distribution)
    result = []
    for class_size in class_distribution:
        your_probability = fractions.Fraction(class_size, total_seats)
        friend_probability = fractions.Fraction(total_seats - class_size, total_seats - 1)
        result.append(your_probability * friend_probability)
    result = ftools.reduce(add, result)
    return result

def main(argv) -> int:
    CLASS_UPPER_SIZE: int = int(input('How many total students are there?                 # ')) # Maximum size of the class* (meaning classes like APUSH or AP Lang, not specific classes)
    CLASS_LOWER_SIZE: int = int(input('What is the smallest a class can get?              # ')) # Minimum size of the class*
    CLASS_DIVISION: int = int(input('How many classes are there?                        # ')) # How many classes there are
    AMOUNT_OF_FRIENDS: int = int(input('How many people do you want to be in a class with? # '))
    arr: list[int] = list(map(calculate_probability, filter(lambda x: ftools.reduce(add, x) == CLASS_UPPER_SIZE, itools.product(range(CLASS_LOWER_SIZE, CLASS_UPPER_SIZE + 1), repeat = CLASS_DIVISION))))
    result = fractions.Fraction(ftools.reduce(add, arr), len(arr)) ** AMOUNT_OF_FRIENDS
    result = float((1 - result) * 100)

    print("-" * 80)
    print(f"There is a {result:.1f}% chance for you to be in a class with at least one of your {AMOUNT_OF_FRIENDS} friend{'s' if AMOUNT_OF_FRIENDS > 1 else ''}, provided that there are {CLASS_DIVISION} class{'es' if CLASS_DIVISION > 1 else ''} each with at least {CLASS_LOWER_SIZE} student{'s' if CLASS_LOWER_SIZE > 1 else ''} and with {CLASS_UPPER_SIZE} student{'s' if CLASS_UPPER_SIZE > 1 else ''} in total.")

    return 0



if __name__ == '__main__':
    sys.exit(main(sys.argv))
