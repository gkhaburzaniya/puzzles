from unittest import TestCase, main


def verify_problem(num, expected_answer):
    module = __import__("Euler{0}".format(num))
    assert module.answer == expected_answer, "{0} != {1}".format(
        module.answer, expected_answer)


class EulerTest(TestCase):

    def test_problem1(self):
        verify_problem(1, 233168)

    def test_problem2(self):
        verify_problem(2, 4613732)

    def test_problem3(self):
        verify_problem(3, 6857)

    def test_problem4(self):
        verify_problem(4, 906609)


if __name__ == "__main__":
    main()
