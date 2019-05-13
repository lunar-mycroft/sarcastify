from time import time
from typing import Optional, Iterator

def _LCG(seed: Optional[int] = None) -> Iterator[int]:
    """
    Generates random numbers via the linear congruential generator algorithm.

    Parameters taken from glibc

    Not meant to be used directly.
    """
    if seed is None:
        seed = int(time())
    x : int = seed
    m : int = 2**31
    a : int = 1664525
    c : int = 1013904223
    while True:
        x = (a*x + c) % m
        yield x

def looksRandom(seed :Optional[int] = None, bias : float = 0.125) -> Iterator[bool]:
    """
    Pseudo random number generator which is biased to produce less continuous segments of 0s or 1s
    """
    bias = int(bias*2**31)
    gen: Iterator[int] = _LCG(seed)

    cutoff: int = 2**30
    for n in gen:
        yield n >= cutoff
        if n > cutoff:
            cutoff += bias
        else:
            cutoff -= bias
        if cutoff<0:
            cutoff = 0
        elif cutoff> 2**31:
            cutoff = 2**31
        cutoff = int(cutoff)

if __name__ == "__main__":
    gen = looksRandom(seed=1993, bias=0.25)
    for _ in range(0,40):
        print(next(gen))