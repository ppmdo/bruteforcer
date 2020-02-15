import unittest
import random

from brute import bruteforce


class TestCorrectRun(unittest.TestCase):

    def setUp(self) -> None:
        """We need to create a list[(str, int)] that contains
        tuples with an identifier and a number. This tuples will have to be combined
        and the number in them summed.

        In between this combinations, we expect a 'true' one: a combination with a sum
        that matches a certain 'target'.

        Example:
            We are looking for a combination that sums 7. So the following universe:
            universe = [('A', 2), ('B', 1), ('C', 5)]

            When used by our "bruteforcer" function, shall return the following:
            result = [(('A', 2), ('C', 5), 0)]
            The last element in the previous list is the 'difference' to the target.

        Features:
            - The bruteforce shall be able to take a "data universe" in the shape specified above,
            the target number and a maximum number of elements to combine. The function shall calculate all possible
            combinations of 1 element up to N number of elements specified and then calculate the possible matching
            combinations.

        Functional specs:
            - The operations involved have to be memory efficient. When the universe is large, and the
            number of combinations grow, we cannot hold them in memory or the system can crash.
            - We expect code to be fast, scalable and in the best case compilable to C.
        """

        self.universe = list()

        for x in range(30):
            i = random.randrange(-1000, 50000)
            self.universe.append((str(x), i))

        # We append 5 known elements for which we know the sum is 4242
        self.universe += [('A', 5000),
                          ('B', 242),
                          ('C', 100),
                          ('D', -100),
                          ('E', -1000)]

    def test_something(self):
        results = bruteforce(self.universe, 4242, 6)

        expected = ((('A', 5000),
                    ('B', 242),
                    ('C', 100),
                    ('D', -100),
                    ('E', -1000)), 0)

        self.assertIn(expected, results)


if __name__ == '__main__':
    unittest.main(module='tests', verbosity=2)
