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


from primepalindrome.primepalindrome import PrimePalindrome

"""
9015110
9989900

3503054
"""

# ---- working { --------
def test_3_13():
    base = 13
    expected = 101

    nextpal = PrimePalindrome(base).nextpal()
    assert nextpal == expected

def test_1_6():
    base = 6
    expected = 7

    nextpal = PrimePalindrome(base).nextpal()
    assert nextpal == expected

def test_2_8():
    base = 8
    expected = 11

    nextpal = PrimePalindrome(base).nextpal()
    assert nextpal == expected

def test_2_1_3503054():
    base = 3503054
    expected = 3515153

    nextpal = PrimePalindrome(base).nextpal()
    assert nextpal == expected
# ---- } working --------

def test_4_9015110():
    base = 9015110
    expected = 9024209

    nextpal = PrimePalindrome(base).nextpal()
    assert nextpal == expected

def test_4_9989900():
    base = 9989900
    expected = 100030001

    nextpal = PrimePalindrome(base).nextpal()
    assert nextpal == expected

