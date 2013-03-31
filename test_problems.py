from unittest import TestCase, main


class EulerTest(TestCase):

    def test_problem1(self):
        from Euler1 import answer
        self.assertEqual(answer, 233168)

    def test_problem2(self):
        from Euler2 import answer
        self.assertEqual(answer, 4613732)

    def test_problem3(self):
        from Euler3 import answer
        self.assertEqual(answer, 6857)

    def test_problem4(self):
        from Euler4 import answer
        self.assertEqual(answer, 906609)


if __name__ == "__main__":
    main()
