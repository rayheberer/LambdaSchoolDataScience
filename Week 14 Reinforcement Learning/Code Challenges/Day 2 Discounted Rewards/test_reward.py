import unittest
from reward import reward


class TestReward(unittest.TestCase):

    def test_always_passing_test(self):
        self.assertEqual(3 + 1, 4)

    def test_reward_1(self):
        self.assertAlmostEqual(reward(-2.1, 0.32), -3.0882352, 3)

    def test_reward_2(self):
	    self.assertAlmostEqual(reward(-0.1, 0.55), -0.222222, 3)

    def test_reward_3(self):
	    self.assertAlmostEqual(reward(3.2, 0.95), 64.0, 3)

    def test_reward_4(self):
	    self.assertAlmostEqual(reward(3.0, 0.79), 14.285714, 3)


if __name__ == '__main__':
    unittest.main()
