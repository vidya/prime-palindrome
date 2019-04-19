"""
https://leetcode.com/problems/prime-palindrome/

866. Prime Palindrome
Medium

Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and
itself, and it is greater than 1.

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same
from left to right as it does from right to left.

For example, 12321 is a palindrome.

Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101


Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
"""

from math import sqrt, ceil


class Primes:
    def __init__(self):
        # primes below 100
        self.primes = [
            2, 3, 5, 7, 11, 13,
            17, 19, 23, 29, 31, 
            37, 41, 43, 47, 53, 
            59, 61, 67, 71, 73, 
            79, 83, 89, 97]

    def is_prime(self, num):
        for p in self.primes:
            if num % p == 0:
                return False

        for x in range(101, ceil(sqrt(num)) + 1, 2):
            if num % x == 0:
                # num is not divisible by any of the previously
                # checked numbers. Hence, x must be a prime.
                self.primes.append(x)

                return False

        return True


class Palindrome:
    def __init__(self, base):
        self.base = base
        if base % 2 == 0:
            self.base += 1

        self.next_start = base

    def __iter__(self):
        return self

    @staticmethod
    def is_pali(s1):
        return s1[0] == s1[-1] and s1[1] == s1[-2] and s1 == s1[::-1]

    def __next__(self):
        x = self.next_start
        while True:
            s1 = str(x)
            if self.is_pali(s1):
                # set starting search number for next invocation of this method
                self.next_start = x + 2
                if x % 2 == 0:
                    self.next_start += 1

                return x

            s1_len = len(s1)

            # extract left half os base num string
            ls1 = s1[:s1_len // 2]

            if s1_len % 2 == 0:
                # base num has an even number of digits
                if ls1[-1] != '9':
                    # increment the last digit
                    new_ls1 = ls1[:-1] + chr(ord(ls1[-1]) + 1)

                    x = int(new_ls1 + new_ls1[::-1])
                    continue

            else:
                # extract the middle digit
                md = s1[s1_len // 2]

                if ord(md) < ord('9'):
                    # increment the middle digit
                    x = int(ls1 + chr(ord(md) + 1) + ls1[::-1])
                    continue

            # check if the next odd number is a palindrome
            x += 2


class PrimePalindrome:
    def __init__(self, base):
        self.base = base

        self.primes = Primes()
        self.palindrome = Palindrome(base)

        self.small_bases = {
            1: 2,
            2: 2,
            3: 3,
            4: 5,
            5: 5,
            6: 7,
            7: 7,
            8: 11,
            9: 11,
            10: 11,
            11: 11,
        }

    def nextpal(self):
        if self.base in self.small_bases:
            return self.small_bases[self.base]

        for x in self.palindrome:
            if self.primes.is_prime(x):
                return x

