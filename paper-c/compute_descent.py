#!/usr/bin/env python3
"""
compute_descent.py
==================

Compute first-descent (T, B) statistics for the compressed Collatz map
S(n) = (3n+1)/2^v_2(3n+1) on positive odd integers.

This script is the data source for Tables 4.1 and 4.2 in paper-c.

Conventions (matching paper-c):
- Compressed Collatz map S takes ODD n to ODD n.
- For odd n>=3, the length of first descent T_des(n) is the smallest
  T>=1 such that S^T(n) < n. Set B = sum of v_2(3 S^{i-1}(n)+1) for
  i=1..T.
- Worst-case ratio in bit-bin k is the smallest B/T over all odd n
  in Omega_k = [2^(k-1), 2^k).
"""

from math import log2
from fractions import Fraction
from random import Random


def first_descent(n: int):
    """Return (T, B) for first descent of compressed Collatz from odd n.

    Iterates S(m) = (3m+1)/2^{v_2(3m+1)} starting at m=n until m<n.
    Returns (T, B) where T is the number of steps and B is the
    cumulative 2-adic valuation along the descent.
    """
    assert n % 2 == 1 and n >= 3
    m = n
    T = 0
    B = 0
    while True:
        u = 3 * m + 1
        v = (u & -u).bit_length() - 1  # v_2(u)
        m = u >> v
        T += 1
        B += v
        if m < n:
            return T, B


def exhaustive_worst(k: int):
    """Return (worst_n, T, B) achieving min B/T over Omega_k."""
    best_ratio = None
    best = None
    lo = 1 << (k - 1)
    hi = 1 << k
    if lo % 2 == 0:
        lo += 1
    for n in range(lo, hi, 2):
        if n < 3:
            continue
        T, B = first_descent(n)
        r = Fraction(B, T)
        if best_ratio is None or r < best_ratio:
            best_ratio = r
            best = (n, T, B)
    return best, best_ratio


def sampled_worst(k: int, rng_seed: int = 42, n_random: int = 10000,
                  prev_worst_n: int | None = None):
    """Structured sample for large k: Mersenne / trailing-1 patterns,
    near-Mersenne, prev-round expansion, plus random odd integers.
    """
    lo = 1 << (k - 1)
    hi = 1 << k
    rng = Random(rng_seed + k)
    candidates = set()

    # (a) trailing-1 patterns: 2^k - 1 and 2^k * m' - 1 (truncated to bin)
    # Mersenne 2^k - 1
    candidates.add((1 << k) - 1)
    # n = 2^j * m' - 1 with various tail lengths j and small odd m'
    # we want n in Omega_k = [2^(k-1), 2^k); 2^k - 1 already covered.
    # Add  n = 2^(k-1) + (2^j - 1) for j = 1..k-1 (a "1-tail" inside bin)
    for j in range(1, k):
        n = (1 << (k - 1)) | ((1 << j) - 1)
        if n % 2 == 1 and lo <= n < hi:
            candidates.add(n)
    # 65 * 2^(k-7) - 1 (small constant-times-power-of-two minus one)
    if k >= 8:
        n = 65 * (1 << (k - 7)) - 1
        if lo <= n < hi and n % 2 == 1:
            candidates.add(n)

    # (b) all-ones tail of length k inside bin (already handled via 2^k-1)
    # near-Mersenne mosaic: n congruent to -1 mod 2^(k-6) within bin
    # cap to avoid huge enumeration
    if k <= 24:
        mod = 1 << max(1, k - 6)
        n = ((lo - 1) // mod + 1) * mod - 1
        while n < hi:
            if n % 2 == 1 and n >= 3:
                candidates.add(n)
            n += mod
    else:
        # for larger k, sample 256 "-1 mod 2^(k-6)" integers
        mod = 1 << (k - 6)
        n = ((lo - 1) // mod + 1) * mod - 1
        added = 0
        while n < hi and added < 256:
            if n % 2 == 1 and n >= 3:
                candidates.add(n)
                added += 1
            n += mod

    # (c) prev-round expansion: small odd multiples of prev worst n
    if prev_worst_n is not None:
        for mult in (2, 3, 5, 7, 9):
            n = mult * prev_worst_n
            if not (n & 1):
                n += 1  # nearest odd
            while n < hi:
                if n >= lo and n % 2 == 1:
                    candidates.add(n)
                n *= 2
                if not (n & 1):
                    n += 1

    # (d) random odd in Omega_k
    for _ in range(n_random):
        n = rng.randrange(lo | 1, hi, 2)
        candidates.add(n)

    best_ratio = None
    best = None
    for n in candidates:
        if n < 3:
            continue
        T, B = first_descent(n)
        r = Fraction(B, T)
        if best_ratio is None or r < best_ratio:
            best_ratio = r
            best = (n, T, B)
    return best, best_ratio, len(candidates)


def main():
    print("=" * 72)
    print("E1: Exhaustive worst-case first-descent ratio per bit-bin k")
    print("=" * 72)
    print(f"{'k':>3} {'#Omega_k':>10} {'worst_n':>14} {'T':>4} {'B':>4} "
          f"{'B/T':>8} {'reduced':>14} {'decimal':>10}")
    prev_worst_n = None
    for k in range(5, 22):
        (n, T, B), ratio = exhaustive_worst(k)
        size = (1 << (k - 1)) // 2 if k >= 2 else 1
        # number of odd n in [2^(k-1), 2^k): exactly 2^(k-2) for k>=2
        size = 1 << max(0, k - 2)
        red = ratio  # already Fraction in lowest terms
        print(f"{k:>3} {size:>10} {n:>14} {T:>4} {B:>4} "
              f"{B}/{T:<6} {red.numerator}/{red.denominator:<10} "
              f"{float(ratio):>10.6f}")
        prev_worst_n = n

    print()
    print("=" * 72)
    print("E3: Structured sampling worst case for k = 22..44")
    print("=" * 72)
    print(f"{'k':>3} {'#cands':>10} {'worst_n':>22} {'T':>4} {'B':>4} "
          f"{'B/T':>10} {'reduced':>10} {'decimal':>10}")
    for k in range(22, 45):
        # try multiple seeds and keep the worst
        best_ratio = None
        best = None
        ncand_total = 0
        for seed in range(3):
            (n, T, B), r, nc = sampled_worst(
                k, rng_seed=seed * 100, n_random=15000,
                prev_worst_n=prev_worst_n)
            ncand_total += nc
            if best_ratio is None or r < best_ratio:
                best_ratio = r
                best = (n, T, B)
        n, T, B = best
        ratio = best_ratio
        print(f"{k:>3} {ncand_total:>10} {n:>22} {T:>4} {B:>4} "
              f"{B}/{T:<8} {ratio.numerator}/{ratio.denominator:<6} "
              f"{float(ratio):>10.6f}")
        prev_worst_n = n

    print()
    print("=" * 72)
    print("E2: First-descent (T, B) for Mersenne 2^k - 1")
    print("=" * 72)
    print(f"{'k':>3} {'n = 2^k - 1':>22} {'T':>4} {'B':>4} {'B/T':>10} "
          f"{'decimal':>10}")
    for k in [5, 10, 15, 20, 25, 30, 41, 44]:
        n = (1 << k) - 1
        T, B = first_descent(n)
        ratio = Fraction(B, T)
        print(f"{k:>3} {n:>22} {T:>4} {B:>4} "
              f"{B}/{T:<8} {float(ratio):>10.6f}")

    print()
    print("=" * 72)
    print("Reference: deterministic floor B(T) = floor(T*log2(3)) + 1")
    print("=" * 72)
    print(f"{'T':>4} {'B(T)':>5} {'B/T':>10}")
    for T in [1, 3, 5, 17, 29, 41, 82, 94, 147]:
        B = int(T * log2(3)) + 1
        print(f"{T:>4} {B:>5} {B}/{T} = {B/T:.6f}")


if __name__ == "__main__":
    main()
