from typing import Iterator
#import click
import sys

from looksRandom import looksRandom

def sarcastify(string : str) -> Iterator[str]:
    rng : Iterator[bool] = looksRandom(bias = 0.25)
    yield string[0]
    for char in string[1:]:
        if not char.isalpha():
            yield char
            continue
        yield char.upper() if next(rng) else char.lower()
    
        

def main(string: str):
    print("".join(sarcastify(string)))

if __name__ == "__main__":
    main(' '.join(sys.argv[1:]))