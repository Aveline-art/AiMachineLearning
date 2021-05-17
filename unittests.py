import unittest
import hog
import random

test_dice_result_1 = [5, 1, 4, 4, 5, 1, 2, 4, 4, 3, 6, 2, 1, 5, 4, 3, 1, 2, 6, 3, 1, 4, 2, 5, 3, 4, 4, 3, 6, 3, 4, 2, 6, 3, 6, 3, 2, 4, 2, 4, 5, 4, 1, 5, 1, 2, 2, 2, 3, 5, 3, 2, 3, 6, 5, 4, 4, 4, 1, 6, 5, 3, 5, 2, 2, 4, 2, 1, 1, 4, 3, 5, 6, 1, 5, 1, 2, 4, 5, 3, 5, 2, 1, 1, 4, 2, 2, 3, 4, 4, 4, 2, 6, 3, 2, 5, 5, 2, 1, 3]
test_dice_result_2 = [3, 1, 1, 5, 3, 4, 4, 5, 3, 2, 6, 2, 3, 4, 1, 2, 5, 4, 1, 1, 1, 6, 4, 4, 1, 5, 6, 6, 4, 3, 1, 2, 1, 5, 3, 6, 2, 5, 2, 6, 3, 5, 3, 5, 3, 6, 3, 5, 1, 4, 2, 6, 4, 5, 4, 6, 6, 2, 2, 2, 5, 3, 6, 5, 2, 5, 1, 1, 1, 4, 1, 5, 3, 5, 3, 5, 3, 1, 3, 3, 5, 3, 4, 5, 2, 3, 2, 1, 5, 1, 6, 4, 2, 3, 5, 2, 6, 5, 1, 4]

test_rolls_result_1 = [3, 1, 4, 5, 4, 5, 3, 3, 5, 4]
test_rolls_result_2 = [3, 5, 1, 3, 4, 1, 4, 3, 6, 6]

class TestHog(unittest.TestCase):

    def test_dice(self):
        random.seed(10)
        results = [hog.dice(6)() for i in range(100)]
        self.assertEqual(results, test_dice_result_1, "test_dice_result_1 does not match")
        random.seed(23)
        results = [hog.dice(6)() for i in range(100)]
        self.assertEqual(results, test_dice_result_2, "test_dice_result_2 does not match")
    
    def test_rolls(self):
        random.seed(47)
        self.assertEqual(hog.rolls(10, hog.dice(6)), test_rolls_result_1, "test_rolls_result_1 does not match")
        random.seed(98)
        self.assertEqual(hog.rolls(10, hog.dice(6)), test_rolls_result_2, "test_rolls_result_2 does not match")

    def test_sow_sad(self):
        self.assertTrue(hog.sow_sad([1, 2, 3]) == 1, "[1, 2, 3] did not equal 1")
        self.assertFalse(hog.sow_sad([4, 5, 6]) == 1, "[4, 5, 6] should not equal 1")
    
    def test_piggy_points(self):
        self.assertTrue(hog.piggy_points(3839127312983721) == 4, "3839127312983721 should equal 4")
        self.assertFalse(hog.piggy_points(38391273129830721) == 1, "38391273129830721 should not equal 1")
        self.assertTrue(hog.piggy_points(9) == 84, "9 should  equal 84")


if __name__ == '__main__':
    unittest.main()
