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

    def test_problem5(self):
        verify_problem(5, 232792560)

    def test_problem6(self):
        verify_problem(6, 25164150)

    def test_problem7(self):
        verify_problem(7, 104743)

    def test_problem8(self):
        verify_problem(8, 40824)

    def test_problem9(self):
        verify_problem(9, 31875000)

    def test_problem10(self):
        verify_problem(10, 142913828922)

    def test_problem11(self):
        verify_problem(11, 70600674)

    def test_problem12(self):
        verify_problem(12, 76576500)

    def test_problem13(self):
        verify_problem(13, 5537376230)

    def test_problem14(self):
        verify_problem(14, 837799)

    def test_problem15(self):
        verify_problem(15, 137846528820)

if __name__ == "__main__":
    main()
