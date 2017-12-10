import unittest
import problems


class TestProblems(unittest.TestCase):

    def test_problem1(self):
        actual = problems.problem1.sum_of_multiples_of(10)
        self.assertEquals(actual, 23)

        actual = problems.problem1.sum_of_multiples_of(1000)
        self.assertEquals(actual, 233168)


if __name__ == '__main__':
    unittest.main()
