import unittest
import hog
import random

test_dice_result_1 = [5, 1, 4, 4, 5, 1, 2, 4, 4, 3, 6, 2, 1, 5, 4, 3, 1, 2, 6, 3, 1, 4, 2, 5, 3, 4, 4, 3, 6, 3, 4, 2, 6, 3, 6, 3, 2, 4, 2, 4, 5, 4, 1, 5, 1, 2, 2, 2, 3, 5, 3, 2, 3, 6, 5, 4, 4, 4, 1, 6, 5, 3, 5, 2, 2, 4, 2, 1, 1, 4, 3, 5, 6, 1, 5, 1, 2, 4, 5, 3, 5, 2, 1, 1, 4, 2, 2, 3, 4, 4, 4, 2, 6, 3, 2, 5, 5, 2, 1, 3]
test_dice_result_2 = [3, 1, 1, 5, 3, 4, 4, 5, 3, 2, 6, 2, 3, 4, 1, 2, 5, 4, 1, 1, 1, 6, 4, 4, 1, 5, 6, 6, 4, 3, 1, 2, 1, 5, 3, 6, 2, 5, 2, 6, 3, 5, 3, 5, 3, 6, 3, 5, 1, 4, 2, 6, 4, 5, 4, 6, 6, 2, 2, 2, 5, 3, 6, 5, 2, 5, 1, 1, 1, 4, 1, 5, 3, 5, 3, 5, 3, 1, 3, 3, 5, 3, 4, 5, 2, 3, 2, 1, 5, 1, 6, 4, 2, 3, 5, 2, 6, 5, 1, 4]

test_rolls_result_1 = [3, 1, 4, 5, 4, 5, 3, 3, 5, 4]
test_rolls_result_2 = [3, 5]

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
        self.assertEqual(hog.rolls(10, hog.dice(6)), min(test_rolls_result_1), "test_rolls_result_1 does not match")
        random.seed(98)
        self.assertEqual(hog.rolls(2, hog.dice(6)), sum(test_rolls_result_2), "test_rolls_result_2 does not match")
    
    def test_piggy_points(self):
        self.assertFalse(hog.piggy_points(3839127312983721) == 1, "3839127312983721 should not equal 1")
        self.assertTrue(hog.piggy_points(938) == 7, "38391273129830721 should equal 19")
        self.assertTrue(hog.piggy_points(9) == 4, "9 should equal 4")
        self.assertTrue(hog.piggy_points(10) == 3, "10 should equal 3")
        self.assertFalse(hog.piggy_points(76) == 25, " 67 should not equal 25")
        self.assertTrue(hog.piggy_points(77) == 5, " 77 should equal 7")
    
    def test_scoring(self):
        # Adds 27 = sum([2, 2, 3, 4, 2, 3, 4, 4, 3])
        # random.seed(33)
        # print(sum(hog.rolls(9, hog.dice(4))))
        # Adds 1 from results [2, 2, 3, 4, 2, 3, 4, 4, 3, 1])
        # random.seed(33)
        # print(sum(hog.rolls(10, hog.dice(4))))
        random.seed(33)
        self.assertEqual(hog.scoring(9, 50, hog.dice(4)), 27, "turn should bring 27 points")
        random.seed(33)
        self.assertEqual(hog.scoring(10, 50, hog.dice(4)), 1, "turn should bring 1 point")
        random.seed(33)
        self.assertEqual(hog.scoring(0, 94, hog.dice(4)), 6, "turn should bring 6 points")
    
    def test_more_boar(self):
        self.assertTrue(hog.more_boar(3472, 4599), "3472 should take another turn against 4599")
        self.assertFalse(hog.more_boar(7, 4599), "7 should not take another turn against 4599")
        self.assertFalse(hog.more_boar(32, 33), "32 should not take another turn against 33")
    
    def test_time_trot(self):
        self.assertTrue(hog.time_trot(7, 63, False), "7 dice on turn 63 should take another turn")
        self.assertFalse(hog.time_trot(8, 56+8, False), "8 dice should never take another turn")
        self.assertFalse(hog.time_trot(9, 56+9, False), "9 dice should never take another turn")
        self.assertFalse(hog.time_trot(10, 56+10, False), "10 dice should never take another turn")
        self.assertFalse(hog.time_trot(1, 9, True), "if last turn was a time trot, never take another turn")
    
    def test_next_player(self):
        self.assertTrue(hog.next_player(0) == 1, "next player is 0")
        self.assertTrue(hog.next_player(1) == 0, "next player is 1")
        self.assertFalse(hog.next_player(0) == 0, "next player is 1")
        self.assertFalse(hog.next_player(1) == 1, "next player is 0")

if __name__ == '__main__':
    unittest.main()
