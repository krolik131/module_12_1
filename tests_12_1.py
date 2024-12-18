import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        t1 = runner.Runner('mp')
        for i in range(10):
            t1.walk()
        self.assertEqual(t1.distance, 50)

    def test_run(self):
        t2 = runner.Runner('uid')
        for i in range(10):
            t2.run()
        self.assertEqual(t2.distance, 100)

    def test_challenge(self):
        t3 = runner.Runner('hutran')
        t4 = runner.Runner('another')
        for i in range(10):
            t3.run()
            t4.walk()
        self.assertNotEqual(t3.distance, t4.distance)

if __name__ == '__main__':
    unittest.main()
