import unittest
import random

from bruteforcer import bruteforce


class TestCorrectRun(unittest.TestCase):

    def setUp(self) -> None:
        self.universe = list()

        for x in range(50):
            i = random.randrange(-1000, 50000)
            self.universe.append((str(x), i))

        # We append 5 known elements for which we know the sum is 4242
        self.universe += [('A', 5000),
                          ('B', 242),
                          ('C', 100),
                          ('D', -100),
                          ('E', -1000)]

    def test_correct(self):
        results = bruteforce(self.universe, 4242, 6)

        expected = ((('A', 5000),
                    ('B', 242),
                    ('C', 100),
                    ('D', -100),
                    ('E', -1000)), 0)

        self.assertIn(expected, results)


if __name__ == '__main__':
    unittest.main(module='tests', verbosity=2)
